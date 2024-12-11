import { Text, View, ScrollView, TextInput, TouchableOpacity, Alert, ImageBackground } from "react-native";
import { useState } from "react";
import { UserqrStyle } from "../styles/UserqrStyle";

export default function Userqr(){

    const saveNote = () => {
        if (!codigo.trim() || !contraseña.trim()) {
            // Mostrar alerta si algún campo está vacío
            Alert.alert('Error', 'Por favor, complete todos los campos antes de continuar.');
            return;
        }

        // Si ambos campos están llenos, navegar a la siguiente pantalla
        
        navigation.navigate('Userqr');
    };

    return(
        <ScrollView contentContainerStyle={UserqrStyle.scrollContainer}>
                <ImageBackground source={require('../assets/fondo.png')} 
                style={UserqrStyle.background}>

                <View>
                    <Text style={UserqrStyle.tittle}>Atten<Text style={UserqrStyle.highlight} >zio</Text> </Text>
                    <Text style={UserqrStyle.welcome}>Bienvenido "inserte nombre" </Text>
                </View>

                <View style={UserqrStyle.main}>
                    
                    <Text style={UserqrStyle.desc}>escanea el codigo para reconocer la clase en la que te encuentras</Text>

                    

                        <TouchableOpacity onPress={saveNote} style={UserqrStyle.button}>
                            <Text style={UserqrStyle.buttonText}>Ingresar</Text>
                        </TouchableOpacity>
                    
                </View>
                </ImageBackground>
            </ScrollView>
        )
}
    


