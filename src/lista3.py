import cv2
import os
import numpy
	
 # Local onde recebe a imagem1 passando o caminho. Imagem no formato JPEG
leitor_da_imagem1 = cv2.imread("../input/imagem1.jpeg", 1)

 # Local onde recebe a imagem2 passando o caminho. Imagem no formato JPEG
leitor_da_imagem2 = cv2.imread("../input/imagem2.jpeg", 1)      

# For responsavem por faze a operacao entre vetores de tamanhos iguais, 
# pois so da para operar dois vetores juntos se ambos foremdo forem do mesmo tamanho. Aqui tera um produto interno com escalarem de 0 a 6. 
# inversamento em um o que e no outro
for i in range(0, 6):
	nova_imagem = leitor_da_imagem1*(i/float(5)) + leitor_da_imagem2*(1-i/float(5))
	
	cv2.imwrite("../output/Output%d.jpg" % (i + 1), nova_imagem)




