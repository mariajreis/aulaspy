{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#menu  de formula\n",
    "\n",
    "# 0 - Sair\n",
    "# 1 - Pitagoras\n",
    "# 2 - Bhaskara\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2083919110.py, line 17)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[23], line 17\u001b[1;36m\u001b[0m\n\u001b[1;33m    else:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "\n",
    "x=int(input('digite um numero de 0 a 2 , ENTER'))\n",
    "print(x)\n",
    "\n",
    "if x==0:\n",
    "    print('Sair')\n",
    "\n",
    "elif x==1:\n",
    "    print('formula pitagoras')\n",
    "    cateto=int(input('digite o valor do cateto oposto'))\n",
    "    cateto2=int(input('digite o valor do cateto adjacente'))\n",
    "\n",
    "h=(cateto**2 + cateto2 **2)**(1/2)\n",
    "\n",
    "print(f'{h}')\n",
    "\n",
    "\n",
    "else:\n",
    "    print('formular de Bhaskara')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.0\n"
     ]
    }
   ],
   "source": [
    "#h2 = (cateto **2 + cateto2 **2)**2\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "delta\n"
     ]
    }
   ],
   "source": [
    "#bhaskara  delta=b2 - 4.a.c   x= -b += Vdelta\n",
    " \n",
    "a=int(input('digite o valor de a'))\n",
    "b=int(input('digite o valor de b'))\n",
    "c=int(input('digite o valor de c'))\n",
    "\n",
    "delta=b**2 -4*a*c\n",
    "\n",
    "print(f'{delta}')\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.10.11"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
