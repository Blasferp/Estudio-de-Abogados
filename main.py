import streamlit as st
import pandas as pd
import datetime
import openpyxl
# import streamlit_image_coordinates
from streamlit_option_menu import option_menu
from datetime import datetime
import plotly.express as px
# import altair as alt
import matplotlib.pyplot as plt
# import requests
from PIL import Image
from io import BytesIO
from datetime import datetime


# Obtener la fecha actual en español
meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

dias_semana = [
    "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"
]

now = datetime.now()
current_date = f"{dias_semana[now.weekday()]}, {now.day} de {meses[now.month - 1]} de {now.year}"


# Mostrar la fecha en la barra lateral
st.sidebar.title(f'📅 Fecha:')
st.sidebar.markdown(
    f'<h2 style="color: #333;">{current_date}</h2>',
    unsafe_allow_html=True
)

# Cambiar el fondo de color del sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #000;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Separar con línea horizontal
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Configuración del menú principal en la barra lateral
with st.sidebar:

    # Configuración del menú principal en la barra lateral
    selected = option_menu(
        menu_title='Menu Principal',
        options=['Principal', 'Vencimientos', 'Juicios', 'Procesos', 'Clientes','Abogados',  'Gastos y Cobros', 'Escritos'],
        menu_icon='gear',
        icons=['', '', '', '', '', '', '', '']
,
        default_index=0,
        orientation='vertical',
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "red", "font-size": "16px"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "lightblue"},
        }
    )


###########################################################################################################


# Mostrar contenido específico según la opción seleccionada
if selected == 'Principal':
    st.title("Bienvenido Luciano! 👋")
    st.markdown(
        """
    Bienvenido a nuestra plataforma diseñada especialmente para estudios de abogados que buscan optimizar su gestión y aumentar su eficiencia operativa.

    Nuestra aplicación ofrece un entorno integrado donde puedes acceder y gestionar todos los aspectos críticos de tu práctica legal. Desde el seguimiento de juicios y casos, la gestión de clientes y abogados, hasta el control de los procesos de cobro pendientes, nuestra herramienta te brinda las funcionalidades necesarias para llevar tu estudio al siguiente nivel.

    Con un diseño intuitivo y fácil de usar, podrás navegar por las diferentes secciones de la aplicación para acceder rápidamente a la información relevante. Además, nuestra plataforma te permite agregar, modificar y eliminar datos con total seguridad y precisión, garantizando una gestión eficaz de tu práctica legal.

    Únete a nosotros en esta experiencia digital diseñada para impulsar tu éxito profesional y ofrecer un servicio excepcional a tus clientes. Descubre cómo nuestra aplicación puede transformar la forma en que gestionas tu estudio de abogados y maximiza el potencial de tu equipo. ¡Estamos aquí para ayudarte a alcanzar tus metas y superar tus expectativas! JAJAJAJAJJAJAJAJA
    """
    )

############################################################################################################


if selected == 'Vencimientos':
    # Título de la aplicación
    st.title("Visualización de Vencimientos")
    st.image('vencimientos.jpg')
    st.write('\n')
   

    # Función para cargar el DataFrame de vencimientos desde un archivo Excel
    def cargar_df_vencimientos():
        try:
            df_vencimientos = pd.read_excel("Vencimientos.xlsx")
        except FileNotFoundError:
            df_vencimientos = pd.DataFrame(columns=['Nº Exp', 'Objeto', 'Fecha', 'Control', 'Fecha Vencimiento'])
        return df_vencimientos

    # Función para guardar el DataFrame en un archivo Excel
    def guardar_df(df, file_name='Vencimientos.xlsx'):
        df.to_excel(file_name, index=False)

    # Función para cargar el DataFrame de procesos desde un archivo Excel
    def cargar_df_procesos():
        try:
            df_procesos = pd.read_excel("Procesos.xlsx")
        except FileNotFoundError:
            df_procesos = pd.DataFrame(columns=['Nº Exp', 'Nº Proceso', 'Objeto', 'Prueba', 'Movimiento', 'Comentarios', 'Notificacion', "Exp Fisico", 'Archivo Adjunto', 'Cobro', 'Gasto', 'Fecha', 'Control', 'Fecha Vencimiento'])
        
        # Convertir la columna 'Fecha Vencimiento' a datetime si no lo está
        if 'Fecha Vencimiento' in df_procesos.columns:
            df_procesos['Fecha Vencimiento'] = pd.to_datetime(df_procesos['Fecha Vencimiento'], errors='coerce')
        
        return df_procesos

    # Cargar los DataFrames
    df_vencimientos = cargar_df_vencimientos()
    df_procesos = cargar_df_procesos()

    # Verificar si hay vencimientos para el día de hoy
    hoy = datetime.now().date()

    # Verificar si la columna 'Fecha Vencimiento' es de tipo datetime
    if 'Fecha Vencimiento' in df_procesos.columns and pd.api.types.is_datetime64_any_dtype(df_procesos['Fecha Vencimiento']):
        vencimientos_hoy = df_procesos[df_procesos['Fecha Vencimiento'].dt.date == hoy]

        if not vencimientos_hoy.empty:
            vencimientos_info = "\n".join(f"N° Expediente: {expediente} (Proceso: {proceso})" for expediente, proceso in zip(vencimientos_hoy['Nº Exp'].astype(str), vencimientos_hoy['Nº Proceso'].astype(str)))
            st.warning(f"Hoy hay vencimientos:\n{vencimientos_info}", icon="⚠️")
            # Mostrar el DataFrame de vencimientos hoy
            st.subheader("Detalles de los vencimientos para hoy")
            st.dataframe(vencimientos_hoy)
            
        else:
            st.info("No hay vencimientos para hoy.")
    else:
        st.error("La columna 'Fecha Vencimiento' no es de tipo datetime en el DataFrame de procesos.")



#############################################################################################################

elif selected == 'Juicios':

    # Título de la aplicación
    st.title("Gestión de Juicios -")
    st.image('derecho-penal.jpg')
    st.write('\n')
    st.subheader('Selecciona una Opcion', help=None)
    
    

    # Función para cargar el DataFrame desde un archivo CSV
    def cargar_df():
        try:
            df_juicios = pd.read_excel("Juicios.xlsx")
        except FileNotFoundError:
            df = pd.DataFrame(columns=['CLIENTE', 'ABOGADO', 'FUERO', 'SEC', 'OGA', 'CAM/SEC', 'Nº EXP', 'FECHA', 'PRUEBA', 'ACTOR', 'CONTRA', 'DEMANDADO', 'SOBRE', 'OBJETO', 'MOVIMIENTO', 'COMENTARIOS', 'CONTROL', 'ESTADO'])
        return df_juicios

    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df_juicios(df_juicios):
        df_juicios.to_excel("Juicios.xlsx", index=False)
        
        
    # Función para cargar el DataFrame desde un archivo CSV
    def cargar_df_fuero():
        try:
            df_fuero = pd.read_excel("Fueros.xlsx")
        except FileNotFoundError:
            df_fuero = pd.DataFrame(columns=['FUERO'])
        return df_fuero

    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df_fuero(df_fuero):
        df_fuero.to_excel("Fueros.xlsx", index=False)

    # Cargar el DataFrame al inicio de la aplicación
    df_juicios = cargar_df()
    df_fuero = cargar_df_fuero()
          
    # Se crean variables para luego combinarlas
    df_clientes = pd.read_excel('Clientes.xlsx')
    df_empresas = pd.read_excel('Empresas.xlsx')
    df_abogados = pd.read_excel('Abogados.xlsx')

    # Crear las Series combinadas
    df_nombre_cliente = df_clientes['Apellido'] + ' ' + df_clientes['Nombre Completo']
    df_nombre_empresa = df_empresas['Nombre de la Empresa']
    df_nombre_abogados = df_abogados['Apellido'] + ' ' + df_abogados['Nombre Completo']
    
    # Concatenar las Series en una sola columna de un nuevo DataFrame
    df_cliente_empresa = pd.concat([df_nombre_cliente, df_nombre_empresa], ignore_index=True)
    df_cliente_empresa = pd.DataFrame(df_cliente_empresa, columns=['Cliente'])
    df_nombre_abogados = pd.DataFrame(df_nombre_abogados, columns=['Abogado'])
    
    # Asegurarse de que todos los valores sean cadenas de texto y eliminar espacios en blanco
    df_cliente_empresa['Cliente'] = df_cliente_empresa['Cliente'].astype(str).str.strip()
    
    # Ordenar la columna 'Cliente' alfabéticamente, ignorando mayúsculas y minúsculas
    df_cliente_empresa = df_cliente_empresa.sort_values(by='Cliente', key=lambda col: col.str.lower()).reset_index(drop=True)
    

    opcion = st.radio("Selecciona una Opcion",
        ["Juicios", "Crear Juicios", "Agregar Informacion"],
        key="Juicios", horizontal=True,label_visibility="collapsed")

    if opcion == "Juicios":
        st.write('***********')
        st.title("Juicios")
        st.write("Selecciona el N° de Expediente para obtener la informacion del juicio que deseas.")
        juicios = st.selectbox("**Numero de Expediente**", df_juicios["Nº EXP"], index=None, placeholder="Elija una opcion")
        
        # Filtrar el DataFrame por el Nº de Expediente seleccionado
        juicio_seleccionado = df_juicios[df_juicios["Nº EXP"] == juicios]

        
        # Filtrar el DataFrame por el Nº de Expediente seleccionado
        abogado_seleccionado = df_juicios[df_juicios["Nº EXP"] == juicios]
        
        if not abogado_seleccionado.empty:
            col1, col2 = st.columns(2)



            with col1:
                st.write('\n')
                st.info(f'**CLIENTE:** {abogado_seleccionado.iloc[0]["CLIENTE"]}')
                st.info(f'**ABOGADO:** {abogado_seleccionado.iloc[0]["ABOGADO"]}')
                st.info(f'**FUERO:** {abogado_seleccionado.iloc[0]["FUERO"]}')
                st.info(f'**OGA:** {abogado_seleccionado.iloc[0]["OGA"]}')

                                
                
                
            with col2:
                st.write('\n')
                st.info(f'**SEC:** {abogado_seleccionado.iloc[0]["SEC"]}')
                st.info(f'**CAM/SEC:** {abogado_seleccionado.iloc[0]["CAM/SEC"]}')                                
                st.info(f'**Nº EXP:** {abogado_seleccionado.iloc[0]["Nº EXP"]}')
                st.info(f'**FECHA:** {abogado_seleccionado.iloc[0]["FECHA"]}')


        else:
            st.warning(f"No se encontró  el Nombre de {juicios}'.")
        

        # Se genera un DataFrame con menos Columnas
        df_juicios_acotado = df_juicios[['CLIENTE', 'ABOGADO', 'FUERO', 'SEC', 'OGA', 'CAM/SEC', 'Nº EXP', 'ACTOR', 'DEMANDADO', 'FECHA']]
        
        # Titulo de la DataFrame
        st.write('*************')
        st.header('Informacion del Total de Juicios')
        st.write(df_juicios_acotado)
        
        
        # Función para descargar como archivo XLSX
        def download_excel(df, file_name='data.xlsx'):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False)
            excel_data = output.getvalue()
            return excel_data

        # Convertir el DataFrame a XLSX
        excel_data = download_excel(df_juicios_acotado)

        # Botón de descarga
        st.download_button(
            label="Download data as XLSX",
            data=excel_data,
            file_name="juicios.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        
        
        
        # Filtrado del DataFrame general
        st.write('*********')
        st.header('Filtrado de Juicios')
        
        columnas_seleccionadas = st.multiselect("Selecciona las Columnas que deseas analizar", df_juicios_acotado.columns.tolist())
        
        if columnas_seleccionadas:
            # Filtrar el DataFrame según las columnas seleccionadas
            df_filtrado = df_juicios[columnas_seleccionadas]
            
            # Mostrar el DataFrame filtrado en Streamlit
            st.dataframe(df_filtrado)
            
            # Función para descargar el DataFrame filtrado como archivo XLSX
            def download_excel(df, file_name='data.xlsx'):
                output = BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                excel_data = output.getvalue()
                return excel_data
            
            # Convertir el DataFrame filtrado a XLSX
            excel_data = download_excel(df_filtrado)
            
            # Botón de descarga para el DataFrame filtrado
            st.download_button(
                label="Download data as XLSX",
                data=excel_data,
                file_name="juicios_filtrado.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        else:
            st.info("Selecciona al menos una columna para filtrar y descargar.")
        
    elif opcion == "Crear Juicios":
        st.write('***********')
        st.title("Crear Crear Juicios")
        st.write("Complete el formulario para agregar un nuevo Crear Juicios.")                 
    
        
            
        with st.form(key="form_ingresar_procesos", clear_on_submit=False, border=True ):
            cliente = st.selectbox("Cliente", df_cliente_empresa["Cliente"], index=None, placeholder="Elija una opcion")
            abogado = st.selectbox("Abogado", df_nombre_abogados ['Abogado'], index=None, placeholder="Elija una opcion")
            fuero = st.selectbox("Fuero", df_fuero['FUERO'], index=None, placeholder="Elija una opcion")
            sec = st.number_input("Sección", min_value=None, value=None, step=1, placeholder="Escribe un número")
            oga = st.number_input("OGA", min_value=None, value=None, step=1, placeholder="Escribe un número")
            cam_sec = st.text_input("CAM/SEC")
            n_exp = st.number_input("N° Expediente", min_value=None, value=None, step=1, placeholder="Escribe un número")            
            actor = st.selectbox("Actor", df_cliente_empresa["Cliente"], index=None, placeholder="Elija una opcion")            
            demandado = st.selectbox("Demandado", df_cliente_empresa["Cliente"], index=None, placeholder="Elija una opcion")
            fecha = st.date_input("Fecha Juicio", value=datetime.today(), format="DD/MM/YYYY")

            
            # Botón para enviar el formulario
            submit = st.form_submit_button("Guardar")

            # Guardar los datos en el DataFrame si se ha enviado el formulario
            if submit:
                if not all([cliente, abogado, fuero, sec, oga, cam_sec, n_exp, actor, demandado, fecha]):
                    st.warning("Todos los campos son obligatorios. Por favor, llene todos los campos.")
                # Verificar si el número de expediente ya existe
                elif n_exp in df_juicios["Nº EXP"].values:
                    st.warning(f"El N° Expediente '{n_exp}' ya existe. Intente con otro número.")    
               
                else:
                    #Crear nueva fila con los datos ingresados
                    nueva_fila = {
                    'CLIENTE': cliente,
                    'ABOGADO': abogado,
                    'FUERO': fuero,
                    'SEC': sec,
                    'OGA': oga,
                    'CAM/SEC': cam_sec,
                    'Nº EXP': n_exp,
                    'FECHA': fecha,                    
                    'ACTOR': actor,                    
                    'DEMANDADO': demandado
                    }

                    
                    # Convertir el diccionario en una lista de diccionarios
                    lista_nuevas_filas = [nueva_fila]

                    # Convertir la lista de diccionarios en un DataFrame
                    df_nuevas_filas = pd.DataFrame(lista_nuevas_filas)
                    
                    # Concatenar el DataFrame original con el nuevo DataFrame
                    df_juicios = pd.concat([df_juicios, df_nuevas_filas], ignore_index=True)

                    # Guardar el DataFrame actualizado
                    guardar_df(df_juicios)
                    st.success(f"Nuevo Juicio agregado.")
                    st.write(df_nuevas_filas)

    
    elif opcion == "Agregar Informacion":
        st.write('***********')
        st.title("Crear Tipo de Fuero")
        st.write("Complete el formulario para agregar un nuevo Fuero.")
          
                    
               
        with st.form(key="form_agregar_informacion", clear_on_submit=True):
            tipo_fuero_nuevo = st.text_input("Tipo Fueros")
            
            # Se crea el boton para guardar
            submit_button = st.form_submit_button("Guardar")

            if submit_button:
                if not tipo_fuero_nuevo:
                    st.warning("El campo Tipo de Cobro es obligatorio. Por favor, llene el campo.")
                else:
                    nueva_fila = {
                        'FUERO': tipo_fuero_nuevo
                    }
                    # Convertir el diccionario en un DataFrame
                    df_nuevas_filas = pd.DataFrame([nueva_fila])
                    
                    # Concatenar el DataFrame original con el nuevo DataFrame
                    df_fuero = pd.concat([df_fuero, df_nuevas_filas], ignore_index=True)

                    # Guardar el DataFrame actualizado
                    guardar_df_fuero(df_fuero)
                    st.success("Se agregó un nuevo tipo de Fueros.")
                    st.write(df_nuevas_filas)
    
#########################################################################################################

elif selected == 'Procesos':
    # Título de la aplicación
    st.title("Procesos en el Juicio")    
    st.image('procesos.jpg')
    st.write('\n')
    st.subheader('Selecciona una Opcion', help=None)  
    
    # Función para cargar el DataFrame de procesos
    def cargar_df_procesos():
        try:
            df_procesos = pd.read_excel("Procesos.xlsx")
        except FileNotFoundError:
            df_procesos = pd.DataFrame(columns=['Nº Exp', 'Nº Proceso', 'Objeto', 'Prueba', 'Movimiento', 'Comentarios', 'Notificacion', "Exp Fisico", 'Archivo Adjunto', 'Cobro', 'Gasto', 'Fecha', 'Control', 'Fecha Vencimiento'])
        return df_procesos

    # Función para guardar el DataFrame en un archivo Excel
    def guardar_df_procesos(df):
        df.to_excel("Procesos.xlsx", index=False)
        
    # Función para cargar el DataFrame de juicios
    def cargar_df_juicios():
        try:
            df_juicios = pd.read_excel("Juicios.xlsx")
        except FileNotFoundError:
            df_juicios = pd.DataFrame(columns=['CLIENTE', 'ABOGADO', 'FUERO', 'SEC', 'OGA', 'CAM/SEC', 'Nº EXP', 'FECHA', 'PRUEBA', 'ACTOR', 'CONTRA', 'DEMANDADO', 'SOBRE', 'OBJETO', 'MOVIMIENTO', 'COMENTARIOS', 'CONTROL', 'FECHA VENCIMIENTO'])
        return df_juicios
    
    # Función para cargar el DataFrame de procesos
    def cargar_df_movimiento():
        try:
            df_movimiento = pd.read_excel("Movimientos.xlsx")
        except FileNotFoundError:
            df_movimiento = pd.DataFrame(columns=['Movimiento'])
        return df_movimiento

    # Función para guardar el DataFrame en un archivo Excel
    def guardar_df_movimiento(df):
        df.to_excel("Movimientos.xlsx", index=False)
        
    # Función para cargar el DataFrame de procesos
    def cargar_df_exp_fisico():
        try:
            df_exp_fisico = pd.read_excel("Exp Fisico.xlsx")
        except FileNotFoundError:
            df_exp_fisico = pd.DataFrame(columns=['Movimiento'])
        return df_exp_fisico

    # Función para guardar el DataFrame en un archivo Excel
    def guardar_df_exp_fisico(df):
        df.to_excel("Exp Fisico.xlsx", index=False)
    
    # Cargar los DataFrames
    df_procesos = cargar_df_procesos()
    df_juicios = cargar_df_juicios()
    df_movimiento = cargar_df_movimiento()
    df_exp_fisico = cargar_df_exp_fisico()
    
    opcion = st.radio("Selecciona una Opcion",
                      ["Procesos", "Crear Procesos", "Agregar Informacion"],
                      key="Procesos", horizontal=True, label_visibility="collapsed")

    if opcion == "Procesos":
        st.subheader('', divider='gray')
        st.title("Procesos")
        st.write("Selecciona el N° de Expediente para obtener la informacion del Procesos que deseas.")
        
        proceso = st.selectbox("**Nº de Expediente**", df_juicios["Nº EXP"].unique(), index=None, placeholder="Elija una opcion")

        # Filtrar el DataFrame por el Nº de Expediente seleccionado
        proceso_seleccionado = df_procesos[df_procesos["Nº Exp"] == proceso]

        if not proceso_seleccionado.empty:
            proceso_numero = st.selectbox("**Nº de Proceso**", proceso_seleccionado["Nº Proceso"].unique(), index=None, placeholder="Elija una opción")

            # Mostrar la información del proceso seleccionado
            proceso_detalle = proceso_seleccionado[proceso_seleccionado["Nº Proceso"] == proceso_numero]
            if not proceso_detalle.empty:
                # Fusionar información de juicios y procesos
                juicio_detalle = df_juicios[df_juicios["Nº EXP"] == proceso]
                proceso_detalle = proceso_detalle.merge(juicio_detalle, left_on="Nº Exp", right_on="Nº EXP", suffixes=('_proceso', '_juicio'))

                col1, col2, col3 = st.columns(3)
                
                



                with col1:
                    st.write('\n')
                    st.info(f'**CLIENTE:** {proceso_detalle.iloc[0]["CLIENTE"]}')
                    st.info(f'**OBJETO:** {proceso_detalle.iloc[0]["Objeto"]}')
                    st.info(f'**NOTIFICACION:** {proceso_detalle.iloc[0]["Notificacion"]}')
                    st.info(f'**GASTO:** {proceso_detalle.iloc[0]["Gasto"]}')
                    # st.info(f'**Movimiento:** {proceso_detalle.iloc[0]["Movimiento_proceso"]}')
                    # st.info(f'**Comentarios:** {proceso_detalle.iloc[0]["Comentarios"]}')
                    # st.info(f'**ABOGADO:** {proceso_detalle.iloc[0]["ABOGADO"]}')

                with col2:
                    st.write('\n')
                    st.info(f'**ACTOR:** {proceso_detalle.iloc[0]["ACTOR"]}')
                    st.info(f'**PRUEBA:** {proceso_detalle.iloc[0]["Prueba"]}')
                    st.info(f'**EXP FISICO:** {proceso_detalle.iloc[0]["Exp Fisico"]}')
                    st.info(f'**COBRO:** {proceso_detalle.iloc[0]["Cobro"]}')


                with col3:
                    st.write('\n')
                    st.info(f'**DEMANDADO:** {proceso_detalle.iloc[0]["DEMANDADO"]}')
                    st.info(f'**MOVIMIENTO:** {proceso_detalle.iloc[0]["Movimiento"]}')
                    st.info(f'**CONTROL:** {proceso_detalle.iloc[0]["Control"]}')
                    st.info(f'**FECHA VENCIMIENTO:** {proceso_detalle.iloc[0]["Fecha Vencimiento"]}')

                
                st.text_area('COMENTARIOS', proceso_detalle.iloc[0]["Comentarios"])
                st.text_area('ARCHIVO ADJUNTO', proceso_detalle.iloc[0]["Archivo Adjunto"])
                    
                # Checkbox para marcar como controlado
                controlado = st.checkbox("Marcar como controlado")

                if controlado:
                    # Update the control date in the DataFrame
                    control_fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    df_procesos.loc[(df_procesos["Nº Exp"] == proceso) & (df_procesos["Nº Proceso"] == proceso_numero), "Control"] = control_fecha
                    guardar_df_procesos(df_procesos)
                    st.success(f"Fecha de control actualizada a {control_fecha}.")
                    st.write(df_procesos[df_procesos["Nº Proceso"] == proceso_numero])
            else:
                st.warning("No se encontró el proceso seleccionado.")
        else:
            st.warning("No se encontraron procesos para el Nº de Expediente seleccionado.")

        st.write("***************")
        st.header("Total de Procesos")
        st.write(df_procesos)
        
        # Función para descargar el DataFrame filtrado como archivo XLSX
        def download_excel(df, file_name='data.xlsx'):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False)
            excel_data = output.getvalue()
            return excel_data
            
        # Convertir el DataFrame filtrado a XLSX
        excel_data = download_excel(df_procesos)
            
        # Botón de descarga para el DataFrame filtrado
        st.download_button(
            label="Download data as XLSX",
            data=excel_data,
            file_name="Procesos.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        
        st.write("***************")
        
        st.header('Filtrado de Columnas de Procesos')

        columnas_seleccionadas = st.multiselect("Selecciona las Columnas que deseas filtrar", df_procesos.columns.tolist())
        
        if columnas_seleccionadas:
            # Filtrar el DataFrame según las columnas seleccionadas
            df_filtrado = df_procesos[columnas_seleccionadas]
            
            # Mostrar el DataFrame filtrado en Streamlit
            st.dataframe(df_filtrado)
            
            # Función para descargar el DataFrame filtrado como archivo XLSX
            def download_excel(df, file_name='data.xlsx'):
                output = BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                excel_data = output.getvalue()
                return excel_data
            
            # Convertir el DataFrame filtrado a XLSX
            excel_data = download_excel(df_filtrado)
            
            # Botón de descarga para el DataFrame filtrado
            st.download_button(
                label="Download data as XLSX",
                data=excel_data,
                file_name="Procesos_columnas_filtradas.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        else:
            st.info("Selecciona al menos una columna para filtrar y descargar.")
        
        
    
    elif opcion == "Crear Procesos":
        st.subheader('', divider='gray')
        st.title("Crear Procesos")
        st.write("Complete el formulario para agregar un nuevo proceso.")   
         
        with st.form(key="form_crear_procesos", clear_on_submit=False):
            n_exp = st.selectbox("Numero de Expediente", df_juicios['Nº EXP'], index=None)
            
            # Calcular el siguiente número de proceso para el expediente seleccionado
            if not df_procesos[df_procesos['Nº Exp'] == n_exp].empty:
                proceso_siguiente = df_procesos[df_procesos['Nº Exp'] == n_exp]['Nº Proceso'].max() + 1
                
            else:
                proceso_siguiente = 1
            
            n_proceso = proceso_siguiente
            objeto = st.text_input("Objeto sobre la demanda")            
            prueba = st.text_input("Prueba")
            movimiento = st.selectbox("Movimiento", df_movimiento["Movimiento"], index=None, placeholder="Elija una opcion")
            comentarios = st.text_input("Comentarios")
            notificacion = st.text_input("Notificacion", placeholder="Ejemplo: av. Salta 778")
            exp_fisico = st.selectbox("Expediente Fisico", df_exp_fisico['Exp Fisico'], index=None)
            fecha = st.date_input('Fecha', value=datetime.today())
            control = st.date_input("Control Fecha", value=None, format="DD/MM/YYYY")
            estado = st.selectbox("Estado", ['En Proceso', 'Finalizado'], index=None)
            archivo_adjunto = st.file_uploader("Subir Archivo Adjunto")
            fecha_vencimiento = st.date_input("Fecha Vencimiento", value=None, format="DD/MM/YYYY")
            
            # Se crea el boton para guardar
            submit_button = st.form_submit_button("Guardar")

            if submit_button:
                if not all([n_exp, objeto, prueba, movimiento, comentarios, notificacion, exp_fisico, control, estado]):
                    st.warning("Todos los campos son obligatorios. Por favor, llene todos los campos.")
                else:
                    nueva_fila = {
                        'Nº Exp': n_exp,
                        'Nº Proceso': n_proceso,
                        'Objeto': objeto,
                        'Prueba': prueba,
                        'Movimiento': movimiento,
                        'Comentarios': comentarios,
                        'Notificacion': notificacion,
                        'Exp Fisico': exp_fisico,
                        'Archivo Adjunto': archivo_adjunto.name if archivo_adjunto else None,
                        'Fecha': fecha,
                        'Control': control,
                        'Estado': estado,
                        'Fecha Vencimiento': fecha_vencimiento
                    }
                    # Convertir el diccionario en un DataFrame
                    df_nuevas_filas = pd.DataFrame([nueva_fila])

                    # Concatenar el DataFrame original con el nuevo DataFrame
                    df_procesos = pd.concat([df_procesos, df_nuevas_filas], ignore_index=True)

                    # Guardar el DataFrame actualizado
                    guardar_df_procesos(df_procesos)
                    st.success("Se agregó un nuevo proceso.")
                    st.write(df_nuevas_filas)
    
    
    elif opcion == "Agregar Informacion":
        st.write('***********')
        st.title("Crear Movimientos")
        st.write("Complete el formulario para agregar un nuevo Movimiento.")
        
        with st.form(key="form_agregar_Movimiento", clear_on_submit=True):
            tipo_movimiento_nuevo = st.text_input("Tipo Movimiento")
            
            # Se crea el boton para guardar
            submit_button = st.form_submit_button("Guardar")

            if submit_button:
                if not tipo_movimiento_nuevo:
                    st.warning("El campo Tipo de Movimiento es obligatorio. Por favor, llene el campo.")
                else:
                    nueva_fila = {
                        'Movimiento': tipo_movimiento_nuevo
                    }
                    # Convertir el diccionario en un DataFrame
                    df_nuevas_filas = pd.DataFrame([nueva_fila])
                    
                    # Concatenar el DataFrame original con el nuevo DataFrame
                    df_movimiento = pd.concat([df_movimiento, df_nuevas_filas], ignore_index=True)

                    # Guardar el DataFrame actualizado
                    guardar_df_movimiento(df_movimiento)
                    st.success("Se agregó un nuevo tipo de Movimiento.")
                    st.write(df_nuevas_filas)
        
        
           
        st.write('***********')
        st.title("Crear ubicacion Expediente Fisico")
        st.write("Complete el formulario para agregar una nueva ubicacion de Expediente Fisico.")
        
        with st.form(key="form_agregar_exp_fisico", clear_on_submit=True):
            tipo_exp_fisico_nuevo = st.text_input("Tipo Exp Fisico")
            
            # Se crea el boton para guardar
            submit_button = st.form_submit_button("Guardar")

            if submit_button:
                if not tipo_exp_fisico_nuevo:
                    st.warning("El campo Tipo de Expediente Fisico es obligatorio. Por favor, llene el campo.")
                else:
                    nueva_fila = {
                        'Exp Fisico': tipo_exp_fisico_nuevo
                    }
                    # Convertir el diccionario en un DataFrame
                    df_nuevas_filas = pd.DataFrame([nueva_fila])
                    
                    # Concatenar el DataFrame original con el nuevo DataFrame
                    df_exp_fisico = pd.concat([df_exp_fisico, df_nuevas_filas], ignore_index=True)

                    # Guardar el DataFrame actualizado
                    guardar_df_exp_fisico(df_exp_fisico)
                    st.success("Se agregó una ubicacion de Expediente Fisico.")
                    st.write(df_nuevas_filas)
                  
#########################################################################################################

elif selected == 'Clientes':
    
    # Título de la aplicación
    st.title("Gestión de Clientes y Empresas - ")
    st.image('cliente_abogado.jpg')
    st.write("\n")
    st.subheader('Selecciona una Opcion')
    
    
    # Función para cargar el DataFrame de clientes
    def cargar_df_clientes():
        try:
            df_clientes = pd.read_excel("Clientes.xlsx")
        except FileNotFoundError:
            df_clientes = pd.DataFrame(columns=[
                'Nombre Completo', 'Apellido', 'Documento', 'Fecha de nacimiento',
                'Nacionalidad', 'Estado civil', 'Dirección', 'Teléfono', 'Email'
            ])
        return df_clientes
    
    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df_clientes(df):
        df.to_excel("Clientes.xlsx", index=False)    

    # Función para cargar el DataFrame de empresas
    def cargar_df_empresas():
        try:
            df_empresas = pd.read_excel("Empresas.xlsx")
        except FileNotFoundError:
            df_empresas = pd.DataFrame(columns=[
                'Nombre de la Empresa', 'Numero de identificacion Fiscal', 'Dirección',
                'Teléfono', 'Email'
            ])
        return df_empresas
    

        
    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df_empresas(df):
        df.to_excel("Empresas.xlsx", index=False)


    # Función para cargar el DataFrame de empresas
    def cargar_df_estado_civil():
        try:
            df_estado_civil = pd.read_excel("Estado Civil.xlsx")
        except FileNotFoundError:
            df_estado_civil = pd.DataFrame(columns=[
                'Estado Civil'
            ])
        return df_estado_civil
    
    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df_estado_civil(df):
        df.to_excel("Estado Civil.xlsx", index=False)

    
    # Función para cargar el DataFrame de empresas
    def cargar_df_nacionalidad():
        try:
            df_nacionalidad = pd.read_excel("Nacionalidad.xlsx")
        except FileNotFoundError:
            df_nacionalidad = pd.DataFrame(columns=[
                'Nacionalidad'
            ])
        return df_nacionalidad
    
    # Función para guardar el DataFrame en un archivo CSV
    def guardar_df_nacionalidad(df):
        df.to_excel("Nacionalidad.xlsx", index=False)


    # Cargar los DataFrames
    df_clientes = cargar_df_clientes()
    df_empresas = cargar_df_empresas()
    df_estado_civil = cargar_df_estado_civil()
    df_nacionalidad = cargar_df_nacionalidad()

    
    opcion = st.radio("Selecciona una Opcion",
        ["Personas", "Empresas", "Crear Persona Fisica", "Crear Empresas", "Agregar Informacion"],
        key="Tabla Clientes", horizontal=True,label_visibility="collapsed")

    if opcion == "Personas":
        st.write('***********')
        st.title("Personas Fisicas")
        st.write("Aquí puedes ver la lista de Personas Fisicas.")
        
        personas = st.selectbox("Cliente", df_clientes["Documento"], index=None, placeholder="Elija una opcion")
        
        # Filtrar el DataFrame por el Nº de Expediente seleccionado
        persona_seleccionado = df_clientes[df_clientes["Documento"] == personas]
        
        if not persona_seleccionado.empty:
            col1, col2 = st.columns(2)

            with col1:
                st.write('\n')
                st.info(f'**NOMBRE:** {persona_seleccionado.iloc[0]["Nombre Completo"]}')
                st.info(f'**APELLIDO:** {persona_seleccionado.iloc[0]["Apellido"]}')
                st.info(f'**DOCUMENTO:** {persona_seleccionado.iloc[0]["Documento"]}')
                st.info(f'**FECHA:** {persona_seleccionado.iloc[0]["Fecha de Nacimiento"]}')                
                
                
            with col2:
                st.write('\n')
                st.info(f'**ESTADO CIVIL:** {persona_seleccionado.iloc[0]["Estado Civil"]}')
                st.info(f'**DIRECCION:** {persona_seleccionado.iloc[0]["Dirección"]}')
                st.info(f'**TELEFONO:** {persona_seleccionado.iloc[0]["Teléfono"]}')
                st.info(f'**EMAIL:** {persona_seleccionado.iloc[0]["Email"]}')
        else:
            st.warning(f"No se encontró ningún juicio con el Nº de Expediente '{personas}'.")
        
        
        st.write('***********') 
        # Titulo de la DataFrame
        st.header('Informacion del Total de Cliente Registrados')
        
        # Se muestra el DataFrame con todos los datos
        st.dataframe(df_clientes)
        
        # Función para descargar el DataFrame filtrado como archivo XLSX
        def download_excel(df, file_name='data.xlsx'):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False)
            excel_data = output.getvalue()
            return excel_data
            
        # Convertir el DataFrame filtrado a XLSX
        excel_data = download_excel(df_clientes)
            
        # Botón de descarga para el DataFrame filtrado
        st.download_button(
            label="Download data as XLSX",
            data=excel_data,
            file_name="Clientes.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        
        st.write("***************")
        
        st.header('Filtrado de Columnas de Clientes')

        columnas_seleccionadas = st.multiselect("Selecciona las Columnas que deseas filtrar", df_clientes.columns.tolist())
        
        if columnas_seleccionadas:
            # Filtrar el DataFrame según las columnas seleccionadas
            df_filtrado = df_clientes[columnas_seleccionadas]
            
            # Mostrar el DataFrame filtrado en Streamlit
            st.dataframe(df_filtrado)
            
            # Función para descargar el DataFrame filtrado como archivo XLSX
            def download_excel(df, file_name='data.xlsx'):
                output = BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                excel_data = output.getvalue()
                return excel_data
            
            # Convertir el DataFrame filtrado a XLSX
            excel_data = download_excel(df_filtrado)
            
            # Botón de descarga para el DataFrame filtrado
            st.download_button(
                label="Download data as XLSX",
                data=excel_data,
                file_name="Clientes_filtrado.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            
        else:
            st.info("Selecciona al menos una columna para filtrar y descargar.")
        
        
    elif opcion == "Empresas":
        st.write('***********')
        st.title("Empresas")
        st.write("Selecciona la Empresas que deseas.")
            
        
        empresa = st.selectbox("**Nombre de la Empresa**", df_empresas["Nombre de la Empresa"], index=None, placeholder="Elija una opcion")
        
        # Filtrar el DataFrame por el Nº de Expediente seleccionado
        empresa_seleccionado = df_empresas[df_empresas["Nombre de la Empresa"] == empresa]
        
        if not empresa_seleccionado.empty:
            col1, col2 = st.columns(2)

            with col1:
                st.write('\n')
                st.info(f'**NOMBRE:** {empresa_seleccionado.iloc[0]["Nombre de la Empresa"]}')
                st.info(f'**CUIT:** {empresa_seleccionado.iloc[0]["Numero de identificacion Fiscal"]}')
                st.info(f'**DOCUMENTO:** {empresa_seleccionado.iloc[0]["Dirección"]}')

                
            with col2:
                st.write('\n')
                st.info(f'**TELEFONO:** {empresa_seleccionado.iloc[0]["Teléfono"]}')
                st.info(f'**EMAIL:** {empresa_seleccionado.iloc[0]["Email"]}')
        else:
            st.warning(f"No se encontró ningún juicio con el Nombre de la Empresa'{empresa}'.")
        
        


        st.write('***********') 
        # Titulo de la DataFrame
        st.header('Informacion del Total de Empresas Registradas')
        
        # Se muestra el DataFrame con todos los datos
        st.dataframe(df_empresas)
        
        # Función para descargar el DataFrame filtrado como archivo XLSX
        def download_excel(df, file_name='data.xlsx'):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False)
            excel_data = output.getvalue()
            return excel_data
            
        # Convertir el DataFrame filtrado a XLSX
        excel_data = download_excel(df_empresas)
            
        # Botón de descarga para el DataFrame filtrado
        st.download_button(
            label="Download data as XLSX",
            data=excel_data,
            file_name="Empresa.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        
        st.write("***************")
        
        st.header('Filtrado de Columnas de Empresas')

        columnas_seleccionadas = st.multiselect("Selecciona las Columnas que deseas filtrar", df_empresas.columns.tolist())
        
        if columnas_seleccionadas:
            # Filtrar el DataFrame según las columnas seleccionadas
            df_filtrado = df_empresas[columnas_seleccionadas]
            
            # Mostrar el DataFrame filtrado en Streamlit
            st.dataframe(df_filtrado)
            
            # Función para descargar el DataFrame filtrado como archivo XLSX
            def download_excel(df, file_name='data.xlsx'):
                output = BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                excel_data = output.getvalue()
                return excel_data
            
            # Convertir el DataFrame filtrado a XLSX
            excel_data = download_excel(df_filtrado)
            
            # Botón de descarga para el DataFrame filtrado
            st.download_button(
                label="Download data as XLSX",
                data=excel_data,
                file_name="Empresa_filtrada.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            
        else:
            st.info("Selecciona al menos una columna para filtrar y descargar.")
        
        
        
    elif opcion == "Crear Persona Fisica":
        st.write('***********')
        st.title("Crear Persona Física")
        st.write("Complete el formulario para agregar una nueva persona física.")   
               
        
        with st.form(key="form_crear_persona_fisica", clear_on_submit=False):
            nombre_completo = st.text_input("Nombre Completo")
            apellido = st.text_input("Apellido")
            documento = st.number_input("Documento de Identidad", min_value=None, value=None, step=1, placeholder="Escribe un número")
            fecha_nacimiento = st.text_input("Fecha de Nacimiento")
            nacionalidad = st.selectbox("Nacionalidad", df_nacionalidad["Nacionalidad"], index=None,placeholder="Elija una opcion")
            estado_civil = st.selectbox("Estado Civil", df_estado_civil["Estado Civil"], index=None, placeholder="Elija una opcion")
            direccion = st.text_input("Dirección",placeholder="Ejemplo: av. Salta 778")
            telefono = st.number_input("Teléfono", min_value=None, value=None, step=1, placeholder="Escribe un número")
            email = st.text_input("Email",placeholder="ejemplo@xmail.com")
            
            # Se crea el boton para guardar
            submit_button = st.form_submit_button("Guardar")

            if submit_button:
                if not all([nombre_completo, apellido, documento, fecha_nacimiento, nacionalidad, estado_civil, direccion, telefono, email]):
                    st.warning("Todos los campos son obligatorios. Por favor, llene todos los campos.")
                # Verificar si el número de expediente ya existe
                elif documento in df_clientes["Documento"].values:
                    st.warning(f"El documento de identidad '{documento}' ya existe. Intente con otro número.")
                    
                else:
                    nueva_fila = {
                        'Nombre Completo': nombre_completo,
                        'Apellido': apellido,
                        'Documento': documento,
                        'Fecha de Nacimiento': fecha_nacimiento,
                        'Nacionalidad': nacionalidad,
                        'Estado Civil': estado_civil,
                        'Dirección': direccion,
                        'Teléfono': telefono,
                        'Email': email
                    }
                    # Convertir el diccionario en una lista de diccionarios
                    lista_nuevas_filas = [nueva_fila]

                    # Convertir la lista de diccionarios en un DataFrame
                    df_nuevas_filas = pd.DataFrame(lista_nuevas_filas)
                    
                    # Concatenar el DataFrame original con el nuevo DataFrame
                    df_clientes = pd.concat([df_clientes, df_nuevas_filas], ignore_index=True)

                    # Guardar el DataFrame actualizado
                    guardar_df_clientes(df_clientes)
                    st.success(f"¡Nuevo Cliente Agregado!.")
                    st.write(df_nuevas_filas)
                    
    elif opcion == "Crear Empresas":
        st.write('***********')
        st.title("Crear Empresas")
        st.write("Complete el formulario para agregar una nueva empresa.")
        
        
        with st.form(key="form_crear_empresa", clear_on_submit=False):
            nombre_empresa = st.text_input("Nombre de la Empresa")
            identificacion_fiscal = st.number_input("Numero de identificacion Fiscal", min_value=None,value=None, step=1, placeholder="Escribe un número")
            direccion_empresa = st.text_input("Dirección",placeholder="Ejemplo: av. Salta 778")
            telefono_empresa = st.number_input("Teléfono", min_value=None,value=None, step=1, placeholder="Escribe un número")
            email_empresa = st.text_input("Email",placeholder="ejemplo@xmail.com")
            
            
            # Se crea el boton para guardar
            submit_button = st.form_submit_button("Guardar")

            if submit_button:
                if not all([nombre_empresa, identificacion_fiscal, direccion_empresa, telefono_empresa, email_empresa]):
                    st.warning("Todos los campos son obligatorios. Por favor, llene todos los campos.")
                # Verificar si el número de expediente ya existe
                elif identificacion_fiscal in df_empresas["Numero de identificacion Fiscal"].values:
                    st.warning(f"El N° Expediente '{identificacion_fiscal}' ya existe. Intente con otro número.")
                    
                else:
                    nueva_fila = pd.DataFrame([{
                        'Nombre de la Empresa': nombre_empresa,
                        'Numero de identificacion Fiscal': identificacion_fiscal,
                        'Dirección': direccion_empresa,
                        'Teléfono': telefono_empresa,
                        'Email': email_empresa
                    }])
                    df_empresas = pd.concat([df_empresas, nueva_fila], ignore_index=True)
                    guardar_df_empresas(df_empresas)
                    st.success("¡Empresa guardada con éxito!")
                    st.write(nueva_fila)
                    
    elif opcion == "Agregar Informacion":
        st.write('***********')
        st.title("Crear Estado Civil")
        st.write("Complete el formulario para agregar un Estado Civil.")
        
        with st.form(key="form_agregar_estado_civil", clear_on_submit=True):
            tipo_estado_civil_nuevo = st.text_input("Tipo Estado Civil")
            
            # Se crea el boton para guardar
            submit_button = st.form_submit_button("Guardar")

            if submit_button:
                if not tipo_estado_civil_nuevo:
                    st.warning("El campo Estado Civil es obligatorio. Por favor, llene el campo.")
                else:
                    nueva_fila = {
                        'Estado Civil': tipo_estado_civil_nuevo
                    }
                    # Convertir el diccionario en un DataFrame
                    df_nuevas_filas = pd.DataFrame([nueva_fila])
                    
                    # Concatenar el DataFrame original con el nuevo DataFrame
                    df_estado_civil = pd.concat([df_estado_civil, df_nuevas_filas], ignore_index=True)

                    # Guardar el DataFrame actualizado
                    guardar_df_estado_civil(df_estado_civil)
                    st.success("Se agregó un nuevo tipo de Estado Civil.")
                    st.write(df_nuevas_filas)
                    
                    
        st.write('***********')
        st.title("Crear Nacionalidad")
        st.write("Complete el formulario para agregar un Nacionalidad.")
        
        with st.form(key="form_agregar_nacionalidad", clear_on_submit=True):
            tipo_nacionalidad_nuevo = st.text_input("Tipo Nacionalidad")
            
            # Se crea el boton para guardar
            submit_button = st.form_submit_button("Guardar")

            if submit_button:
                if not tipo_nacionalidad_nuevo:
                    st.warning("El campo Nacionalidad es obligatorio. Por favor, llene el campo.")
                else:
                    nueva_fila = {
                        'Nacionalidad': tipo_nacionalidad_nuevo
                    }
                    # Convertir el diccionario en un DataFrame
                    df_nuevas_filas = pd.DataFrame([nueva_fila])
                    
                    # Concatenar el DataFrame original con el nuevo DataFrame
                    df_nacionalidad = pd.concat([df_nacionalidad, df_nuevas_filas], ignore_index=True)

                    # Guardar el DataFrame actualizado
                    guardar_df_nacionalidad(df_nacionalidad)
                    st.success("Se agregó un nuevo tipo de Nacionalidad.")
                    st.write(df_nuevas_filas)            
                    
                    
#####################################################################################################   

elif selected == 'Abogados':
    
    # Título de la aplicación
    st.title("Gestión de Abogados -")
    st.image('abogados.jpg')
    st.write('\n')   
    st.subheader('Selecciona una Opcion', help=None)
    
    # Función para cargar el DataFrame de clientes
    def cargar_df_abogados():
        try:
            df_abogados = pd.read_excel("Abogados.xlsx")
        except FileNotFoundError:
            df_abogados = pd.DataFrame(columns=[
                'Nombre Completo', 'Apellido', 'Documento', "Cedula", 'Fecha de Nacimiento',
                'Nacionalidad', 'Estado Civil', 'Dirección', 'Teléfono', 'Email'
            ])
        return df_abogados

        # Función para guardar el DataFrame en un archivo CSV
    def guardar_df(df):
        df.to_excel("Abogados.xlsx", index=False)
    
    
    # Cargar los DataFrames
    df_abogados = cargar_df_abogados()

    
    opcion = st.radio("Selecciona una Opcion",
        ["Abogados", "Crear Abogados", "Agregar Informacion"],
        key="Tabla Clientes", horizontal=True,label_visibility="collapsed")

    if opcion == "Abogados":
        st.subheader('', divider='gray')
        st.title("Abogados")
        st.write("Aquí puedes ver la lista de Abogados.")
        
        abogado = st.selectbox("**Cedula**", df_abogados["Cedula"], index=None, placeholder="Elija una opcion")
        
        # Filtrar el DataFrame por el Nº de Expediente seleccionado
        abogado_seleccionado = df_abogados[df_abogados["Cedula"] == abogado]
        
        if not abogado_seleccionado.empty:
            col1, col2 = st.columns(2)

            with col1:
                st.write('\n')
                st.info(f'**NOMBRE:** {abogado_seleccionado.iloc[0]["Nombre Completo"]}')
                st.info(f'**APELLIDO:** {abogado_seleccionado.iloc[0]["Apellido"]}')
                st.info(f'**DOCUMENTO:** {abogado_seleccionado.iloc[0]["Documento"]}')
                st.info(f'**CEDULA:** {abogado_seleccionado.iloc[0]["Cedula"]}')
                                
                
                
            with col2:
                st.write('\n')
                st.info(f'**FECHA:** {abogado_seleccionado.iloc[0]["Fecha de Nacimiento"]}')
                st.info(f'**ESTADO CIVIL:** {abogado_seleccionado.iloc[0]["Estado Civil"]}')
                st.info(f'**DIRECCION:** {abogado_seleccionado.iloc[0]["Dirección"]}')
                st.info(f'**TELEFONO:** {abogado_seleccionado.iloc[0]["Teléfono"]}')
                st.info(f'**EMAIL:** {abogado_seleccionado.iloc[0]["Email"]}')
        else:
            st.warning(f"No se encontró  el Nombre de {abogado}'.")
        
       
  
        st.write('***********') 
        # Titulo de la DataFrame
        st.header('Informacion del Total de Abogados Registrados')
        
        # Se muestra el DataFrame con todos los datos
        st.dataframe(df_abogados)
        
        # Función para descargar el DataFrame filtrado como archivo XLSX
        def download_excel(df, file_name='data.xlsx'):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False)
            excel_data = output.getvalue()
            return excel_data
            
        # Convertir el DataFrame filtrado a XLSX
        excel_data = download_excel(df_abogados)
            
        # Botón de descarga para el DataFrame filtrado
        st.download_button(
            label="Download data as XLSX",
            data=excel_data,
            file_name="Abogados.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        
        st.write("***************")
        
        st.header('Filtrado de Columnas de Abogados')

        columnas_seleccionadas = st.multiselect("Selecciona las Columnas que deseas filtrar", df_abogados.columns.tolist())
        
        if columnas_seleccionadas:
            # Filtrar el DataFrame según las columnas seleccionadas
            df_filtrado = df_abogados[columnas_seleccionadas]
            
            # Mostrar el DataFrame filtrado en Streamlit
            st.dataframe(df_filtrado)
            
            # Función para descargar el DataFrame filtrado como archivo XLSX
            def download_excel(df, file_name='data.xlsx'):
                output = BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                excel_data = output.getvalue()
                return excel_data
            
            # Convertir el DataFrame filtrado a XLSX
            excel_data = download_excel(df_filtrado)
            
            # Botón de descarga para el DataFrame filtrado
            st.download_button(
                label="Download data as XLSX",
                data=excel_data,
                file_name="Abogados_filtrado.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            
        else:
            st.info("Selecciona al menos una columna para filtrar y descargar.")
        


    elif opcion == "Crear Abogados":
        st.subheader('', divider='gray')
        st.title("Crear Abogados")
        st.write("Complete el formulario para agregar una nueva persona física.")   
                    
                
        with st.form(key="form_crear_abogados", clear_on_submit=True):
            nombre_completo = st.text_input("Nombre Completo", autocomplete=None)
            apellido = st.text_input("Apellido")
            documento = st.number_input("Documento de Identidad", min_value=None, value=None, step=1, placeholder="Escribe un número")
            cedula = st.text_input("Cedula")            
            fecha_nacimiento = st.text_input("Fecha de Nacimiento")
            nacionalidad = st.selectbox("Nacionalidad", ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador", "Paraguay", "Perú", "Uruguay", "Venezuela"], index=None,placeholder="Elija una opcion")
            estado_civil = st.selectbox("Estado Civil", ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a", "Otro"], index=None, placeholder="Elija una opcion")
            direccion = st.text_input("Dirección",placeholder="Ejemplo: av. Salta 778")
            telefono = st.number_input("Teléfono", min_value=None, value=None, step=1, placeholder="Escribe un número")
            email = st.text_input("Email",placeholder="ejemplo@xmail.com")
            
            # Se crea el boton para guardar
            submit_button = st.form_submit_button("Guardar",)

            if submit_button:
                if not all([nombre_completo, apellido, documento, cedula, fecha_nacimiento, nacionalidad, estado_civil, direccion, telefono, email]):
                    st.warning("Todos los campos son obligatorios. Por favor, llene todos los campos.")
                elif n_ced in df_abogados["Cedula"].values:
                    st.warning(f"El N° Expediente '{n_ced}' ya existe. Intente con otro número.")
                else:
                    nueva_fila = {
                        'Nombre Completo': nombre_completo,
                        'Apellido': apellido,
                        'Documento': documento,
                        'Cedula': cedula,
                        'Fecha de Nacimiento': fecha_nacimiento,
                        'Nacionalidad': nacionalidad,
                        'Estado Civil': estado_civil,
                        'Dirección': direccion,
                        'Teléfono': telefono,
                        'Email': email
                    }
                    # Convertir el diccionario en una lista de diccionarios
                    lista_nuevas_filas = [nueva_fila]

                    # Convertir la lista de diccionarios en un DataFrame
                    df_nuevas_filas = pd.DataFrame(lista_nuevas_filas)
                    
                    # Concatenar el DataFrame original con el nuevo DataFrame
                    df_abogados = pd.concat([df_abogados, df_nuevas_filas], ignore_index=True)

                    # Guardar el DataFrame actualizado
                    guardar_df(df_abogados)
                    st.success(f"Se agrego un nuevo Abogado")
                    st.write(df_nuevas_filas)
    
    
    elif opcion == "Agregar Informacion":
        st.write('***********')
        st.title("Crear Persona Física")
        st.write("Complete el formulario para agregar una nueva persona física.")

########################################################################################################################   
    
elif selected == 'Gastos y Cobros':
        
    # Título de la aplicación
    st.title("Visualizacion de Gastos y Cobros")
    st.image('cobro.jpg')
    st.write('\n')
    st.subheader('Selecciona una Opcion', help=None)        

    # Función para cargar el DataFrame de cobros
    def cargar_df_gasto():
        try:
            df_gasto = pd.read_excel("Gastos.xlsx")
        except FileNotFoundError:
            df_gasto = pd.DataFrame(columns=[
                'Tipo de Gasto'
            ])
        return df_gasto
    
    # Función para guardar el DataFrame de cobros
    def guardar_df_gasto(df):
        df.to_excel("Gastos.xlsx", index=False)
        
    
    # Función para cargar el DataFrame de cobros
    def cargar_df_cobros():
        try:
            df_cobros = pd.read_excel("Cobros.xlsx")
        except FileNotFoundError:
            df_cobros = pd.DataFrame(columns=[
                'Tipo de Cobro'
            ])
        return df_cobros
    
    # Función para guardar el DataFrame de cobros
    def guardar_df_cobros(df):
        df.to_excel("Cobros.xlsx", index=False)
    
        
    # Función para cargar el DataFrame de juicios
    def cargar_df_proceso():
        df_proceso = pd.read_excel("Procesos.xlsx")
        return df_proceso
    
    
    
    # Cargar los DataFrames
    df_gasto = cargar_df_gasto()
    df_proceso = cargar_df_proceso()
    df_cobros = cargar_df_cobros()
    
    
    opcion = st.radio("Selecciona una Opcion",
                      ["Gastos", "Cobros", "Crear Tipo de Gastos", "Crear Tipo de Cobros"],
                      key="Tabla Clientes", horizontal=True, label_visibility="collapsed")

    if opcion == "Gastos":
        st.subheader('', divider='gray')
        st.title("Gastos")
        st.write("Aquí puedes ver la lista de Gastos.")
        
        df_gasto_nuevo = df_proceso[['Nº Exp', 'Nº Proceso','Gasto', 'Control']]
       

        # Titulo de la DataFrame
        st.header('Informacion del Total de Gastos Registrados')
        
        # Se muestra el DataFrame con todos los datos
        st.dataframe(df_gasto_nuevo)
        
        # Función para descargar el DataFrame filtrado como archivo XLSX
        def download_excel(df, file_name='data.xlsx'):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False)
            excel_data = output.getvalue()
            return excel_data
            
        # Convertir el DataFrame filtrado a XLSX
        excel_data = download_excel(df_gasto_nuevo)
            
        # Botón de descarga para el DataFrame filtrado
        st.download_button(
            label="Download data as XLSX",
            data=excel_data,
            file_name="Gastos.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        
        st.write("***************")
        
        st.header('Filtrado de Columnas de Gastos')

        columnas_seleccionadas = st.multiselect("Selecciona las Columnas que deseas filtrar", df_gasto_nuevo.columns.tolist())
        
        if columnas_seleccionadas:
            # Filtrar el DataFrame según las columnas seleccionadas
            df_filtrado = df_gasto_nuevo[columnas_seleccionadas]
            
            # Mostrar el DataFrame filtrado en Streamlit
            st.dataframe(df_filtrado)
            
            # Función para descargar el DataFrame filtrado como archivo XLSX
            def download_excel(df, file_name='data.xlsx'):
                output = BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                excel_data = output.getvalue()
                return excel_data
            
            # Convertir el DataFrame filtrado a XLSX
            excel_data = download_excel(df_filtrado)
            
            # Botón de descarga para el DataFrame filtrado
            st.download_button(
                label="Download data as XLSX",
                data=excel_data,
                file_name="Gastos_filtrado.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            
        else:
            st.info("Selecciona al menos una columna para filtrar y descargar.")
        
        
        
    elif opcion == "Cobros":
        
        st.subheader('', divider='gray')
        st.title("Cobros")
        st.write("Aquí puedes ver la lista de Cobros.")
    
        df_cobro_nuevo = df_proceso[['Nº Exp', 'Nº Proceso', 'Cobro', 'Control']]
        
        # Titulo de la DataFrame
        st.header('Informacion del Total de Cobros Registrados')
        
        # Se muestra el DataFrame con todos los datos
        st.dataframe(df_cobro_nuevo)
        
        # Función para descargar el DataFrame filtrado como archivo XLSX
        def download_excel(df, file_name='data.xlsx'):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False)
            excel_data = output.getvalue()
            return excel_data
            
        # Convertir el DataFrame filtrado a XLSX
        excel_data = download_excel(df_cobro_nuevo)
            
        # Botón de descarga para el DataFrame filtrado
        st.download_button(
            label="Download data as XLSX",
            data=excel_data,
            file_name="Cobro.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        
        st.write("***************")
        
        st.header('Filtrado de Columnas de Cobros')

        columnas_seleccionadas = st.multiselect("Selecciona las Columnas que deseas filtrar", df_cobro_nuevo.columns.tolist())
        
        if columnas_seleccionadas:
            # Filtrar el DataFrame según las columnas seleccionadas
            df_filtrado = df_cobro_nuevo[columnas_seleccionadas]
            
            # Mostrar el DataFrame filtrado en Streamlit
            st.dataframe(df_filtrado)
            
            # Función para descargar el DataFrame filtrado como archivo XLSX
            def download_excel(df, file_name='data.xlsx'):
                output = BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                excel_data = output.getvalue()
                return excel_data
            
            # Convertir el DataFrame filtrado a XLSX
            excel_data = download_excel(df_filtrado)
            
            # Botón de descarga para el DataFrame filtrado
            st.download_button(
                label="Download data as XLSX",
                data=excel_data,
                file_name="Cobros_filtrado.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            
        else:
            st.info("Selecciona al menos una columna para filtrar y descargar.")
    
    elif opcion == "Crear Tipo de Gastos":
        st.subheader('', divider='gray')
        st.title("Tipo de Gastos")
        st.write("Complete el formulario para agregar un Nuevo Tipo de Gastos.")
               
        with st.form(key="form_crear_tipo_gastos", clear_on_submit=True):
            tipo_gasto_nuevo = st.text_input("Tipo Gastos")
            
            # Se crea el boton para guardar
            submit_button = st.form_submit_button("Guardar")

            if submit_button:
                if not tipo_gasto_nuevo:
                    st.warning("El campo Tipo de Cobro es obligatorio. Por favor, llene el campo.")
                else:
                    nueva_fila = {
                        'Tipo de Gasto': tipo_gasto_nuevo
                    }
                    # Convertir el diccionario en un DataFrame
                    df_nuevas_filas = pd.DataFrame([nueva_fila])
                    
                    # Concatenar el DataFrame original con el nuevo DataFrame
                    df_gasto = pd.concat([df_gasto, df_nuevas_filas], ignore_index=True)

                    # Guardar el DataFrame actualizado
                    guardar_df_gasto(df_gasto)
                    st.success("Se agregó un nuevo tipo de cobro.")
                    st.write(df_nuevas_filas)
    


    elif opcion == "Crear Tipo de Cobros":
        st.subheader('', divider='gray')
        st.title("Crear Cobros")
        st.write("Complete el formulario para agregar un Nuevo Cobro.")   
                    
               
        with st.form(key="form_crear_tipo_cobro", clear_on_submit=True):
            tipo_cobro_nuevo = st.text_input("Tipo Cobros")
            
            # Se crea el boton para guardar
            submit_button = st.form_submit_button("Guardar")

            if submit_button:
                if not tipo_cobro_nuevo:
                    st.warning("El campo Tipo de Cobro es obligatorio. Por favor, llene el campo.")
                else:
                    nueva_fila = {
                        'Tipo de Cobro': tipo_cobro_nuevo
                    }
                    # Convertir el diccionario en un DataFrame
                    df_nuevas_filas = pd.DataFrame([nueva_fila])
                    
                    # Concatenar el DataFrame original con el nuevo DataFrame
                    df_cobros = pd.concat([df_cobros, df_nuevas_filas], ignore_index=True)

                    # Guardar el DataFrame actualizado
                    guardar_df_cobros(df_cobros)
                    st.success("Se agregó un nuevo tipo de cobro.")
                    st.write(df_nuevas_filas)
    
    
########################################################################################################################     


elif selected == 'Escritos':
    # Título de la aplicación
    st.title("Visualizacion de Vencimientos")
    st.image('vencimientos.jpg')
    st.write('\n')
    st.subheader('Selecciona una Opcion', help=None)