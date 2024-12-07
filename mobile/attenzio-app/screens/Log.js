import { Text, View, ScrollView, TextInput, TouchableOpacity, Alert } from "react-native";
import { useState } from "react";
import { logStyle } from "../styles/logStyle";

export default function Log({navigation}){
    const [codigo, setCodigo] = useState('')
    const [contraseña, setContraseña] = useState('')

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
            <ScrollView contentContainerStyle={logStyle.scrollContainer}>
                <View style={logStyle.main}>
                    <Text style={logStyle.tittle}>iniciar <Text style={logStyle.highlight} >sesion</Text> </Text>
                    <Text style={logStyle.desc}>ingrese su correo estudiantil y contraseña</Text>

                    <View style={logStyle.card}>
                        <TextInput  
                        placeholder='codigo estudiantil' 
                        placeholderTextColor="slategray" 
                        value={codigo} 
                        onChangeText={setCodigo}
                        style={logStyle.input} 
                        />
                    
                        <TextInput  
                        placeholder='contraseña' 
                        placeholderTextColor="slategray" 
                        value={contraseña} 
                        onChangeText={setContraseña}
                        style={logStyle.input} 
                        />

                        <TouchableOpacity onPress={saveNote} style={logStyle.button}>
                            <Text style={logStyle.buttonText}>Ingresar</Text>
                        </TouchableOpacity>
                    </View>
                </View>
            </ScrollView>
        )
}

