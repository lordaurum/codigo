#Autor: Aureliano Vieira da Mota - Nickname: LordAurum
#Código: Abrir Gaveta de dinheiro interligada a ECF - testado com Elgin K
#Extra:Para este exemplo são necessários os arquivos elgin.dll e elgin.ini

import ctypes #este pacote permite chamar dlls
library = ctypes.WinDLL("C:\Python33\elgin.dll")#e possivel indicar qualquer caminho para dll
library.Elgin_AcionaGaveta()#esta funcao e outras podem ser encontradas no site da Elgin no espaco reservado a desenvolvedores

#Com este exemplo podemos endender como utilizar uma dll para o desenvolvimento de aplicações para ECFs - Emissores de Cupom Fiscal
