## ATHENS METRO ##

The proyect consists of three separate files: Main.py, src/interfaz.py, and src/algoritmo.py. The Main.py file imports and uses the classes and functions defined in the other two files to create a graphical user interface (GUI) that allows users to find the shortest path between two metro stations in Athens using the A* algorithm.

# File Structure #

Here's how the code works:

- src/interfaz.py: This file defines the Interfaz class that creates the GUI for the shortest path finder. It uses the tkinter library for creating the GUI and PIL (Python Imaging Library) for displaying an image (map). The GUI prompts the user to enter the names of the start and destination stations, and upon clicking the "OK" button, it calls the A* algorithm (aestrella function from src/algoritmo.py) to find the optimal route and display the results on the map.

- src/algoritmo.py: This file defines the A* algorithm to find the shortest path between two metro stations. It also contains supporting functions to calculate the direct travel time between two nodes using the Haversine formula and other utility functions required for the A* algorithm.

- Main.py: This file imports the Interfaz class from src.interfaz and runs the GUI.

# How to run the code # 

To execute the code, make sure all the files are in the correct directory structure as described above. Then, simply run the Main.py script:

```python
python Main.py
```

The GUI window will open, allowing you to enter the names of the start and destination metro stations. After clicking the "OK" button, it will display the optimal route and the estimated travel time on the map. If the entered station names are invalid or not found, an error message will be displayed.

Please note that to run the code, you will need to have the required Python libraries installed (tkinter, PIL, and numpy). You can install them using pip if you haven't already:

```bash
pip install tkinter
pip install pillow
pip install numpy
```
Ensure that you have the map image ("mapa.png") located in the resources directory, as specified in the src/interfaz.py file.

## Authors

| Name         | Role           | Contact                                           |
|----------------|---------------|------------------------
| Álvaro Domínguez       | Developer | alvarodm2002adm@gmail.com      
| Luis Martin    | Developer     | luis.mceballos@alumnos.upm.es 
| Gonzalo Algaba    | Developer     | gonzalo.algaba@alumnos.upm.es 
| Felipe Susaeta    | Developer     | f.susaeta@alumnos.upm.es        

