import { StyleSheet } from "react-native";

export const homeStyles = StyleSheet.create({
    main:{
        flex:1
    },
    tittle:{
        marginTop:60,
        textAlign:'center',
        fontSize:44,
        fontStyle:'italic',
        fontWeight:'600'
    },
    highlight: {
        color: '#FBBC05', // Estilo para "zio"
        fontWeight: 'bold', // Opcional, si deseas resaltar más
        
    },
    desc:{
        marginTop:60,
        textAlign:'center',
        fontSize:20,
        fontStyle:'italic',
        fontWeight:'600'
    },
    buttonAdd:{
        backgroundColor:'#FBBC05',
        marginHorizontal: 20,
        borderRadius: 20,
        paddingVertical: 5,
        marginTop: 30
    },
    textbuttonadd:{
        color:'black',
        textAlign:'center',
        fontSize:18,
        fontWeight: 'bold'
    },
    background: {
        flex: 1, // Hace que la imagen ocupe todo el espacio disponible
        resizeMode: 'cover', // Ajusta la imagen para cubrir la pantalla
    }
})