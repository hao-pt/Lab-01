from MapState import MapState
from Prob import Prob
from Agent import Agent
import argparse
import sys

parser = argparse.ArgumentParser() # Phan nhap tham so dong lenh
parser.add_argument("input", help="Path to input file", type=str)
parser.add_argument("output", help="Path to output file", type=str)
args = parser.parse_args()
	

#Main driver:
def main(args):
	# Mo file input de lay thong tin
	with open(args.input, "r") as input_file:
	    all_lines = input_file.read().splitlines()
	
	# xoa tat cac khoang trang cua phan ma tran
	for i in range(3, len(all_lines), 1):
	    all_lines[i] = all_lines[i].replace(" ", "")
	
	n = m = int(all_lines[0]) # Lay do dai chieu ngang va chieu doc
	startCoor = all_lines[1].split()
	start = (int(startCoor[0]), int(startCoor[1])) # Lay vi tri cua S
	goalCoor = all_lines[2].split()
	goal = (int(goalCoor[0]), int(goalCoor[1])) # Lay vi tri cua G
	matrix = [] # Lay ma tran the hien ban do duong di
	for i in range(3, len(all_lines), 1):
	    matrix.append(list(all_lines[i]))
	
	#Kiem tra start va goal co phai obstacle hay khong?
	#Neu dung thi in ra -1
	if matrix[start[0]][start[1]] == '1' or matrix[goal[0]][goal[1]] == '1':
		with open(args.output, 'w') as output_file:
			output_file.write('-1')
		sys.exit()
	
	mapState = MapState(n, m, matrix, start, goal)
	problem = Prob(mapState)
	agent = Agent(problem)
	
	result = agent.getPath() # Lay thong so dau ra de ghi file output
	
	with open(args.output, "w") as output_file: # Ghi file output
	    # Kiem tra xem co tim duoc duong di khong
	    if result == -1:
	        output_file.write("-1")
	        sys.exit()
	    # Buoc 1: Xuat so step can de di tu Start den Goal
	    output_file.write(str(result[0]))
	    output_file.write("\n")
	
	    # Buoc 2: Xuat toa do cua cac o can duoc di qua
	    for (i, r) in enumerate(result[1]):
	        output_file.write("("+str(r[0])+","+str(r[1])+")")
	        if i != len(result[1]) - 1:
	            output_file.write(" ")
	    output_file.write("\n")
	
	    # Buoc 3: Xuat ma tran output the hien bang do duong di
	    m = len(result[2]) # do dai chieu doc cua ma tran output
	    n = len(result[2][0]) # do dai chieu ngang cua ma tran output
	    for (i,r1) in enumerate(result[2]):
	        for (j, r2) in enumerate(r1):
	            output_file.write(r2)
	            if j != n - 1:
	                output_file.write(" ")
	        if i != m - 1:
	            output_file.write("\n")
	
if __name__ == '__main__':
	main(args)