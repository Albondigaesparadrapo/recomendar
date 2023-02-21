import streamlit as st
import random

st.header("Recomendaciones")
opcion = st.radio("Escoge tu tipo de pasamiento favorito",("Manual","En línea","Intelectual"))
if opcion == "Manual":
    st.write(random.choice["Pintura","Escritura","Origami"])
if opcion == "En línea":
    opcion_en_linea = st.radio("Escoge:",("Solo","Con amigos"))
    if opcion_en_linea == "Solo":
        st.write(random.choice["Minesweeper","Minecraft","Ver youtube","Ver una película"])
    elif opcion_en_linea == "Con amigos":
        st.write(random.choice["Minecraft","Roblox","Hacer videollamada"])
if opcion == "Intelectual":
    st.write(random.choice["Leer un libro","Hacer un sudoku","Leer el periódico"])
