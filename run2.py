{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a21eb9ed-1ed5-4a84-b853-62b5915a6ed0",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block after function definition on line 29 (2165324392.py, line 32)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[5], line 32\u001b[0;36m\u001b[0m\n\u001b[0;31m    def main():\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m expected an indented block after function definition on line 29\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "\n",
    "from collections import deque\n",
    "\n",
    "\n",
    "# Константы для символов ключей и дверей\n",
    "keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]\n",
    "doors_char = [k.upper() for k in keys_char]\n",
    "\n",
    "\n",
    "def get_input():\n",
    "    \"\"\"Чтение данных из стандартного ввода.\"\"\"\n",
    "    return [list(line.strip()) for line in sys.stdin]\n",
    "\n",
    "\n",
    "def solve(data):\n",
    "    rows, cols = len(data), len(data[0])  # задаем размер сетки\n",
    "    key_found = set() # найденные ключи\n",
    "    robots = []  # координаты четырех роботов\n",
    "    total_keys = 0 # количество ключей в матрице\n",
    "    for i in range(rows):\n",
    "        for j in range(cols):\n",
    "            if mat[i][j]==\"@\":\n",
    "                robots.append((i,j))\n",
    "            if mat[i][j] in keys_char:\n",
    "                total_keys+=1\n",
    "                \n",
    "    way = [(0,1),(1,0),(0,-1),(-1,0)]  # вправо, вниз, влево, вверх\n",
    "    \n",
    "    func = deque([robots])\n",
    "    visit = set(robots)\n",
    "    steps = 0\n",
    "    keys = 0\n",
    "    while func:\n",
    "        x, y = func.popleft()\n",
    "        if keys == total_keys:\n",
    "            return steps\n",
    "        else:\n",
    "            for dx, dy in way:\n",
    "                nx, ny = x + dx, y + dy\n",
    "                if 0 <= nx < rows and 0 <= ny < cols and data[nx][ny] != \"#\" and (nx,ny) not in visit:\n",
    "                    cell = data[nx][ny]\n",
    "                \n",
    "                    if cell in doors_char:\n",
    "                        door = cell.lower()\n",
    "                        if door in found_keys:\n",
    "                            steps += 1\n",
    "                            continue  # Если у нас есть ключ, можем пройти через дверь\n",
    "                        else:\n",
    "                            return steps  # Не можем пройти через дверь\n",
    "\n",
    "                    if cell in keys_char:\n",
    "                        found_keys.add(cell)  # Собираем ключи\n",
    "                        keys += 1 \n",
    "                        steps += 1\n",
    "                    func.append((nx, ny))\n",
    "                    visit.add((nx, ny))\n",
    "    return steps\n",
    "\n",
    "def main():\n",
    "    data = get_input()\n",
    "    result = solve(data)\n",
    "    print(result)\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b327851-b2f9-407f-8877-0b5262ce51c8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
