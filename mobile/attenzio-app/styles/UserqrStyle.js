import { StyleSheet } from "react-native";
export const UserqrStyle = StyleSheet.create({

    scrollContainer:{
        flexGrow:1,
        justifyContent:'center',

    },
    main:{
        flex:1,
        justifyContent:'center',
        alignItems:'center',
        padding:12,
    },
    tittle:{
        fontSize:40,
        fontWeight: '600',
        marginBottom: 8,
        textAlign: 'left',
        marginTop: 50,
        fontStyle: 'italic'

    },
    background: {
        flex: 1, // Hace que la imagen ocupe todo el espacio disponible
        resizeMode: 'cover', // Ajusta la imagen para cubrir la pantalla
    },
    highlight: {
        color: '#FBBC05', 
        fontWeight: 'bold', 
        
    },
    button:{
        width:'100%',
        height: 50,
        borderRadius: 25,
        backgroundColor: '#FBBC05',
        justifyContent: 'center',
        alignItems: 'center',
        marginTop: 20,

    },
    buttonText:{
        color:'black',
        fontSize:18,
        fontWeight:'600',
        textAlign:'center',
    },
    welcome:{
        fontSize:25,
        fontWeight: '600',
        marginBottom: 8,
        textAlign: 'center',
        marginTop: 20,
        fontStyle: 'italic'

    },
    desc:{
        fontSize:15,
        fontWeight: '600',
        marginBottom: 8,
        textAlign: 'center',
        marginTop: 20,
        fontStyle: 'italic'

    }

})