import csv
import pandas as pd
import glob
import os
from NBP_transformer import Currency_file
from NBP_transformer import File_csv_exporter
import seaborn as sns
import matplotlib.pyplot as plt

folder=r"c:/Users/Admin/Desktop/Python/repository_dg/100-days-of-code-in-python/src/day_022/archive_files_for_fx_data/fx_data_from_nbp"
csv_files_list=glob.glob(os.path.join(folder,'*.csv')) # it will find all the  *csv files in the catalog 

# C:\Users\Admin\Desktop\Python\repository_dg\100-days-of-code-in-python\src\day_022\archive_files_for_fx_data\fx_data_from_nbp

for file in csv_files_list:

    print('start processing files')

    fx_foreign_pln=Currency_file(file,"ISO-8859-2",";")

    # print(fx_foreign_pln.show_columns())

    # print(fx_foreign_pln.show_head(5))



    fx_foreign_pln.remove_rows(0)

    # print(fx_foreign_pln.show_head(5))


    fx_foreign_pln.adjust_by_specific_columns('data','1USD','1EUR','1CHF')
    
    fx_foreign_pln.convert_to_date('data').convert_to_number('1USD','1EUR','1CHF')

    fx_foreign_pln.rename_columns(**{"data" : "Date"},**{"1USD":"FX_USD/PLN"},**{'1EUR':"FX_EUR/PLN"},**{'1CHF':"FX_CHF/PLN"})


                                
    # print(fx_foreign_pln.show_columns())
    # print(fx_foreign_pln["FX_USD/PLN"].dtype)

    # fx_foreign_pln.convert_to_number("FX_USD/PLN","FX_EUR/PLN","FX_CHF/PLN")


    folder_out1=r"c:/Users/Admin/Desktop/Python/repository_dg/100-days-of-code-in-python/src/day_022/archive_files_for_fx_data/fx_nbp_data_out"

    out_folder=os.path.join(folder_out1)  #new folder will be created in case it does not exist
    os.makedirs(out_folder,exist_ok=True) # creates a new folder ,exist_ok=True < if the catalog is there, do not treat it as error

    out_file=os.path.join(out_folder,os.path.basename(file)) # it will take only the basename file  which is already there > os.path.basename(file)

    fx_foreign_pln_new = File_csv_exporter(
        fx_foreign_pln,
        out_file, 
        encoding="ISO-8859-2",
        sep=";"
    )


    fx_foreign_pln_new.to_csv()

    print('end file processing')


folder_out=r"c:/Users/Admin/Desktop/Python/repository_dg/100-days-of-code-in-python/src/day_022/archive_files_for_fx_data/fx_nbp_data_out"
all_out_files=glob.glob(os.path.join(folder_out,'*.csv'))

folder_out2=r"c:/Users/Admin/Desktop/Python/repository_dg/100-days-of-code-in-python/src/day_022/archive_files_for_fx_data"
location_of_merged_file=os.path.join(folder_out2,'fx_nbp_merged_out') 
os.makedirs(location_of_merged_file,exist_ok=True)

merged_file_path = os.path.join(location_of_merged_file, "fx_nbp_merged_out.csv")

list_of_files=[]
for filename in all_out_files:
    csv_files=Currency_file(filename,encoding='utf-8',sep=';')
    list_of_files.append(csv_files.ccy_file)

merged_file=pd.concat(list_of_files,ignore_index=False)

# merged_file_out=File_csv_exporter(merged_file,location_of_merged_file)



merged_file.to_csv(merged_file_path,sep=';', encoding='utf-8', index=False)


columns_cov=["FX_USD/PLN","FX_EUR/PLN","FX_CHF/PLN"]
cov_matrix=merged_file[columns_cov].cov()

print(f'Cov matrix is :\n {cov_matrix}')




columns_cov = ["FX_USD/PLN", "FX_EUR/PLN", "FX_CHF/PLN"]

# Macierz korelacji
corr_matrix = merged_file[columns_cov].corr()
print(f'Correlation matrix is: {corr_matrix}')

# Heatmapa korelacji
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Correlation matrix is ")
plt.show()