{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Harshcs21/Artificial_Intelligence/blob/main/pythonTutorial.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Harsh Ghiya\n",
        "1BM21CS073"
      ],
      "metadata": {
        "id": "lefouUOcnDoN"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rGGy_3P7Wgsw",
        "outputId": "7a9c4345-f540-40d7-b173-462e0f7aab02"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the age21\n",
            "adult\n"
          ]
        }
      ],
      "source": [
        "#age criteria\n",
        "age=int(input(\"enter the age \"))\n",
        "if age<=0:\n",
        "  print(\"invalid age!!!\")\n",
        "elif age<=12:\n",
        "  print(\"children\")\n",
        "elif age<=19:\n",
        "  print(\"adolescent\")\n",
        "elif age<65:\n",
        "  print(\"adult\")\n",
        "else:\n",
        "  print(\"older adults\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#multiplication table\n",
        "num=int(input(\"enter a number \"))\n",
        "for i in range(1,11):\n",
        "  print(num,'x',i,'=',num*i)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fcLg1_IMYs3B",
        "outputId": "6a608464-5e53-4ce9-a0c2-dc510b11dfce"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a number5\n",
            "5 x 1 = 5\n",
            "5 x 2 = 10\n",
            "5 x 3 = 15\n",
            "5 x 4 = 20\n",
            "5 x 5 = 25\n",
            "5 x 6 = 30\n",
            "5 x 7 = 35\n",
            "5 x 8 = 40\n",
            "5 x 9 = 45\n",
            "5 x 10 = 50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#pattern\n",
        "num=int(input(\"enter number\"))\n",
        "for i in range(1,num+1):\n",
        "  for j in range(i):\n",
        "    print(i,end=\" \")\n",
        "  print(\"\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O3tYM9mNZRU_",
        "outputId": "afe76e0b-0a7f-4129-f3a1-4a5539ed858e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number8\n",
            "1 \n",
            "2 2 \n",
            "3 3 3 \n",
            "4 4 4 4 \n",
            "5 5 5 5 5 \n",
            "6 6 6 6 6 6 \n",
            "7 7 7 7 7 7 7 \n",
            "8 8 8 8 8 8 8 8 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#pattern\n",
        "num=int(input(\"enter number \"))\n",
        "for i in range(1,num+1):\n",
        "  for j in range(1,i+1):\n",
        "    print(j,end=\" \")\n",
        "  print(\"\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P8VuhR5rae3u",
        "outputId": "2d2ab937-8a45-4cec-b137-1f6a3e9b4771"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number6\n",
            "1 \n",
            "1 2 \n",
            "1 2 3 \n",
            "1 2 3 4 \n",
            "1 2 3 4 5 \n",
            "1 2 3 4 5 6 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#reverse integer\n",
        "num=int(input(\"enter a number \"))\n",
        "sum=0\n",
        "while num!=0:\n",
        "  rem=num%10\n",
        "  sum=sum*10+rem\n",
        "  num=num//10\n",
        "print(\"Reverse=\",sum)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hKeRh1wVfEuO",
        "outputId": "87c74c63-1d6f-4be8-a9d1-b0118e657d6d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a number 635\n",
            "Reverse= 536\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lis=[]\n",
        "l=int(input(\"enter the length of the array \"))\n",
        "print(\"enter numbers \")\n",
        "for i in range(l):\n",
        "  n=int(input())\n",
        "  lis.append(n)\n",
        "for i in range(l-1):\n",
        "  for j in range(l-i-1):\n",
        "    if(lis[j]>lis[j+1]):\n",
        "      lis[j],lis[j+1]=lis[j+1],lis[j]\n",
        "print(\"sorted list\",lis)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q53EVGPhgrP2",
        "outputId": "c5ebe99e-4e66-45c4-ebcb-da33c52ff0d1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the length of the array 6\n",
            "enter numbers \n",
            "9\n",
            "5\n",
            "2\n",
            "1\n",
            "6\n",
            "9\n",
            "sorted list [1, 2, 5, 6, 9, 9]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from itertools import permutations\n",
        "arr=\"2563\"\n",
        "print(list(permutations(arr)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S7Ssy1YpjbT-",
        "outputId": "6f0f67ed-a4cd-44a3-b29b-d21865a55b86"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[('2', '5', '6', '3'), ('2', '5', '3', '6'), ('2', '6', '5', '3'), ('2', '6', '3', '5'), ('2', '3', '5', '6'), ('2', '3', '6', '5'), ('5', '2', '6', '3'), ('5', '2', '3', '6'), ('5', '6', '2', '3'), ('5', '6', '3', '2'), ('5', '3', '2', '6'), ('5', '3', '6', '2'), ('6', '2', '5', '3'), ('6', '2', '3', '5'), ('6', '5', '2', '3'), ('6', '5', '3', '2'), ('6', '3', '2', '5'), ('6', '3', '5', '2'), ('3', '2', '5', '6'), ('3', '2', '6', '5'), ('3', '5', '2', '6'), ('3', '5', '6', '2'), ('3', '6', '2', '5'), ('3', '6', '5', '2')]\n"
          ]
        }
      ]
    }
  ]
}
