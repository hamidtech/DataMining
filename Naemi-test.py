{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "helloworld\n"
     ]
    }
   ],
   "source": [
    "message = \"helloworld\"\n",
    "print (message)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\H_jam\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "os.getcwd()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.11.3 | packaged by Anaconda, Inc. | (main, Apr 19 2023, 23:46:34) [MSC v.1916 64 bit (AMD64)]\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "print(sys.version)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy\n",
    "import scipy\n",
    "import matplotlib\n",
    "import pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n",
      "<class 'numpy.ndarray'>\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "arr = np.array([1, 2, 3, 4, 5])\n",
    "\n",
    "print(arr)\n",
    "\n",
    "print(type(arr))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "ML",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
