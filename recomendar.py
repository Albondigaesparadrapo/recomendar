import streamlit as st
import random

st.header("Recomendaciones")
opcion = st.radio("Escoge tu tipo de pasamiento favorito",("Manual","En línea","Intelectual"))
if opcion == "Manual":
    manual = ["Pintura","Escritura","Origami"]
    st.write(random.choice(manual))
if opcion == "En línea":
    opcion_en_linea = st.radio("Escoge:",("Solo","Con amigos"))
    solo = ["Minesweeper","Minecraft","Ver youtube","Ver una película","ah"]
    if opcion_en_linea == "Solo":
        if opcion_en_linea != "ah":
            st.write(random.choice(solo))
        else:
            st.error("¿No tienes amigos o qué?")
    elif opcion_en_linea == "Con amigos":
        conamigos = ["Minecraft","Roblox","Hacer videollamada"]
        st.write(random.choice(conamigos))
if opcion == "Intelectual":
    intelectual = ["Leer un libro","Hacer un sudoku","Leer el periódico"]
    st.write(random.choice(intelectual))
