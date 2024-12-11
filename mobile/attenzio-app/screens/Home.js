import { Text, View, TouchableOpacity, ImageBackground } from "react-native";
import { homeStyles } from "../styles/homeStyle";

export default function Home({navigation}){
    return(
        <ImageBackground 
            source={require('../assets/fondo.png')} // Ruta correcta hacia la imagen
            style={homeStyles.background} // Estilo para el fondo
        >
            <View style={homeStyles.main}> 
                <Text style={homeStyles.tittle}>
                    Atten
                    <Text style={homeStyles.highlight}>zio</Text>
                </Text>
                <Text style={homeStyles.desc}>
                    Inicia sesión o crea una cuenta para ingresar
                </Text>
                <TouchableOpacity 
                    onPress={() => navigation.navigate('Log')} 
                    style={homeStyles.buttonAdd}
                >
                    <Text style={homeStyles.textbuttonadd}>Iniciar sesión</Text>
                </TouchableOpacity> 
                <TouchableOpacity 
                    onPress={() => navigation.navigate('Register')} 
                    style={homeStyles.buttonAdd}
                >
                    <Text style={homeStyles.textbuttonadd}>Regístrate</Text>
                </TouchableOpacity>  
            </View>
        </ImageBackground>
    )
}

