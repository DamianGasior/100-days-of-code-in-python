logo=r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/'''

""" adding 'r' before the  string does solve this problem : SyntaxWarning: invalid escape sequence '\ '
 this problem is happning when there is a set of symbols which containst '\' which is used for example in :
\n, \t, \\, by adding 'r' at the beginning each the text is not analyzed , its treated a 'raw' string """