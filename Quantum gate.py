#!/usr/bin/env python
# coding: utf-8

# In[1]:


#make sure to install Qiskit 1.2 version for this code to work and compatible Scipy


# In[2]:


from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer


# In[3]:


# Create a quantum circuit with 2 qubits 
qc = QuantumCircuit(2) #chane the qubits needed as required

# Apply Pauli-X gate (quantum NOT) on the qubit
qc.x(1)

# Draw the circuit
qc.draw(output='mpl')


# In[4]:


# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1)

# Apply Hadamard gate on the qubit
qc.h(0)

# Draw the circuit
qc.draw(output='mpl')


# In[5]:


# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply CNOT gate with qubit 0 as control and qubit 1 as target
qc.cx(0, 1)

# Draw the circuit
qc.draw(output='mpl')


# In[ ]:




