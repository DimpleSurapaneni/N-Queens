**Logic for Computer Scientists**
**Project: Satisfiability test of clauses and its application.**


**Problem Statement:**

The N-Queens problem is a well-known combinatorial puzzle involving placing N queens on an N × N chessboard in such a way that no two queens threaten each other. The challenge is to use a SAT (Boolean Satisfiability) solver to translate the N-Queens problem into a set of Boolean variables and constraints. The ultimate objective is to find a solution that satisfies these constraints.

**Project Goals:**
- Formulate the N-Queens problem as a Boolean satisfiability (SAT) instance.
- Utilize a SAT solver to convert the logical constraints into Boolean variables.
- Develop a Python script, e.g., `sat_cnf.py`, to generate the Conjunctive Normal Form (CNF) representation of the N-Queens problem.
- Leverage an established SAT solver, such as minisat, to determine the satisfiability of the formulated CNF.
- Extract and interpret the solution provided by the SAT solver to determine the queen placements that satisfy the N-Queens problem constraints.
**Conjunctive Normal Form:**
Conjunctive normal form (CNF) is a way of representing boolean logic as a conjunction of 
classes. Here each class is an expression of a form and consists of propositional value. 
There are several properties of CNF. Every proposition in a CNF should be either true or 
false. A conjunction of two propositions is a disjunction. A truth value’s compound 
propositions is not dependent on the truth value of a conjunction.
Ex: CNF Representation:
(x1 ∨ y1 ∨ z1) ∧ (x2 ∨ y2 ∨ z2) ∧ (x3 ∨ y3 ∨ z3).

**Softwares and Libraries Used:**
- Initially installed the Linux OS environment in an Oracle VM VirtualBox Manager
- In the Ubuntu terminal installed the minisat using the below commands
  - `sudo apt-get update`
  - `sudo apt-get install minisat`
- A sat solver is generally used to determine whether a propositional logic formula is 
  satisfiable or not.
- It is a software that can handle a text file containing CNF formula as input and 
  returns satisfactory or unsatisfiable results by checking the formula.
- I have written the code to generate the CNF for the n - queens problems in python 
  named as `sat_cnf.py`. 
- We took the reference from [https://huyennguyen.com/n-queens/](https://huyennguyen.com/n-queens/)

**Steps for Execution:**
1. `$ python3 sat_cnf.py` → gives you the cnf file 
2. `$ minisat queens_n.cnf queens_n.out` → runs the cnf file within in the sat solver and 
   saves the output to the output file
3. `$ cat queens_n.out` → to view the output file
