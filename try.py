import customtkinter as ctk
from PIL import Image
import threading
from pymaze import maze, agent, COLOR
# === Configuration ===
ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"
ctk.FontManager.load_font("asset/font/Poppins.ttf")
# === Main Window ===
master = ctk.CTk()
master.title("Rescue Map Algorithm")
master.geometry("800x600")
master.minsize(800, 600)

menu_frame = ctk.CTkFrame(master, fg_color= "transparent", width= 800, height= 600)
title_frame = ctk.CTkFrame(menu_frame, fg_color="blue", corner_radius= 20, bg_color="transparent", height= 200)
title_lbl = ctk.CTkLabel(title_frame, fg_color="blue", text= "Rescue Map Locator", font=("Poppins", 45), text_color= "white")

buttons_frame = ctk.CTkFrame(menu_frame, fg_color="transparent", corner_radius=20, height = 200)
start_button = ctk.CTkButton(buttons_frame, text= "Start", font=("Poppins", 25), command= lambda: change_screen(1))
report_button = ctk.CTkButton(buttons_frame, text= "Report Traffic", font=("Poppins", 25))

title_frame.pack(fill="x", padx= 20, pady=(0,100))
title_frame.pack_propagate(False)
title_lbl.pack(expand= True)

buttons_frame.pack(fill="x", padx= 50)
buttons_frame.pack_propagate(False)
start_button.pack(fill= "x", padx= 10, pady= (0,50))
report_button.pack(fill="x", padx= 10, pady= (0,50))
menu_frame.pack_propagate(False)
menu_frame.pack(expand= True)

location_selection_frame = ctk.CTkFrame(master, fg_color="transparent")
selection_image = Image.open("asset/images/selection_image.png")
selection_img_frm = ctk.CTkFrame(location_selection_frame, fg_color="transparent", border_color= "black", border_width= 5)
selection_img = ctk.CTkImage(selection_image, size=(700,400))
selection_img_holder = ctk.CTkLabel(selection_img_frm, image= selection_img, text= "")
first_btn = ctk.CTkButton(location_selection_frame, text= "Here!", font= ("Poppins", 18), width= 40, bg_color= "black", command= lambda: selected((27,16)))
second_btn = ctk.CTkButton(location_selection_frame, text= "Here!", font= ("Poppins", 18), width= 40, bg_color= "black", command= lambda: selected((38,20)))
third_btn = ctk.CTkButton(location_selection_frame, text= "Here!", font= ("Poppins", 18), width= 40, bg_color= "black", command= lambda: selected((14,32)))
fourth_btn = ctk.CTkButton(location_selection_frame, text= "Here!", font= ("Poppins", 18), width= 40, bg_color= "black", command= lambda: selected((38,36)))
fifth_btn = ctk.CTkButton(location_selection_frame, text= "Here!", font= ("Poppins", 18), width= 40, bg_color= "black", command= lambda: selected((31,46)))
sixth_btn = ctk.CTkButton(location_selection_frame, text= "Here!", font= ("Poppins", 18), width= 40, bg_color= "black", command= lambda: selected((22,61)))
seventh_btn = ctk.CTkButton(location_selection_frame, text= "Here!", font= ("Poppins", 18), width= 40, bg_color= "black", command= lambda: selected((6,61)))
instruction_lbl = ctk.CTkLabel(location_selection_frame, text= "Click the location of caller", font= ("Poppins", 30))

selection_img_frm.pack()
selection_img_holder.pack()
instruction_lbl.pack(pady= 20)
first_btn.place(x= 20, y= 200)
second_btn.place(x= 60, y= 320)
third_btn.place(x= 350, y= 50)
fourth_btn.place(x= 280, y= 280)
fifth_btn.place(x= 480, y= 220)
sixth_btn.place(x= 550, y= 130)
seventh_btn.place(x= 490, y= 80)

accident_type_frm = ctk.CTkFrame(master, fg_color="transparent", width= 600, height = 600)
accident_type_lbl = ctk.CTkLabel(accident_type_frm, fg_color="transparent", text= "Select the severity of accident", font=("Poppins", 30))

accident_type_btn_frm = ctk.CTkFrame(accident_type_frm, fg_color="transparent")
minor_button = ctk.CTkButton(accident_type_btn_frm, text= "Minor Accident", font= ("Poppins", 20), height= 200, width= 200, command= lambda: selected_type("Minor"))
major_button = ctk.CTkButton(accident_type_btn_frm, text= "Major Accident", font= ("Poppins", 20), height= 200, width= 200, command= lambda: selected_type("Major"))
accident_type_btn_frm.pack(fill= "x", padx= 20, expand = True)
minor_button.pack(side= "left", expand= True)
major_button.pack(side="left", expand = True)
accident_type_lbl.pack(pady= 20, expand = True)
accident_type_frm.pack_propagate(False)
(22,61)

# Holder Variables
coordinates = None
def change_screen(screen_number):
    if screen_number == 0:
        menu_frame.pack(expand= True)
    if screen_number == 1:
        menu_frame.forget()
        location_selection_frame.pack(expand = True)

def selected(coord):
    global coordinates
    coordinates = coord
    location_selection_frame.forget()
    accident_type_frm.pack(expand = True)

def selected_type(type_of_accident):
    global coordinates
    master.destroy()
    threading.Thread(target= lambda: run_maze_visualization(coordinates, type_of_accident)).start()
    


def BFS(m, start, goal):
    frontier = [start]
    explored = [start]
    bfsPath = {}
    while len(frontier) > 0:
        currCell = frontier.pop(0)
        if currCell == goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
    else:
        print("Path not found!")
    fwdPath = {}
    cell = goal
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    return fwdPath

def run_maze_visualization(accident_coord, type_of_accident):
    m = maze(40,70)
    m.CreateMaze(loadMaze="maze--2025-05-12--18-11-15.csv")
    hospital_coordinates = [(18,3), (15,7), (10,21), (25,22), (19,22), (11,27), (3,27), (19,29), (9,32), (24,33), (14,45), (30,46), (38,69)]
    police_coordinates = [(15,8), (28,12), (20,14), (13,15), (10,20), (13,22), (20,22), (23,23), (19,28), (6,31), (17,33), (20,40), (24,42), (3,49), (13,50), (10,62)]

    shortest_path = None
    shortest_agent_coord = None

    if type_of_accident == "Major":
        candidates = hospital_coordinates
        agent_color = COLOR.light
    elif type_of_accident == "Minor":
        candidates = police_coordinates
        agent_color = COLOR.red

    for coord in candidates:
        path = BFS(m, coord, accident_coord)
        if path:  # path is not None
            if shortest_path is None or len(path) < len(shortest_path):
                shortest_agent_coord = coord
                shortest_path = path
    # Visualize all candidate agents
    for coord in candidates:
        a = agent(m, x=coord[0], y=coord[1], footprints=True, color=agent_color, filled=True)


    sample_agent_pos = accident_coord
    sample_agent = agent(m, x= sample_agent_pos[0], y=sample_agent_pos[1], footprints=True, color= COLOR.green, filled= True)
    path = BFS(m,sample_agent_pos,shortest_agent_coord)
    m.tracePath({sample_agent: path})
    m.run()

    
# === Run App ===
master.mainloop()
