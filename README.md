# N-Queens
N-Queens python program for minisat
Softwares and Libraries Used:
• Initially installed the Linux OS environment in an Oracle VM VirtualBox Manager
• In the Ubuntu terminal installed the minisat using the below commands
✓ sudo apt-get update
✓ sudo apt-get install minisat
• A sat solver is generally used to determine whether a propositional logic formula is 
satisfiable or not.
• It is a software that can handle a text file containing CNF formula as input and 
returns satisfactory or unsatisfiable results by checking the formula.
• I have written the code to generate the CNF for the n - queens problems in python 
named as sat_cnf.py 
• We took the reference from the https://huyennguyen.com/n-queens/
Steps for Execution: run the below commands.
1. $ python3 sat_cnf.py → gives you the cnf file 
2. $ minisat queens_n.cnf queens_n.out → runs the cnf file within in the sat solver and 
saves the output to the output file
3. $ cat queens_n.out → to view the output file
