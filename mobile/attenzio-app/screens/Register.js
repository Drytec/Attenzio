import { Text, View, ScrollView, TextInput, TouchableOpacity } from "react-native";
import { useState } from "react";
import { registerStyle } from "../styles/registerStyle";

export default function Register(navigation){
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
            <ScrollView contentContainerStyle={registerStyle.scrollContainer}>
                <View style={registerStyle.main}>
                    <Text style={registerStyle.tittle}>iniciar <Text style={registerStyle.highlight} >sesion</Text> </Text>
                    <Text style={registerStyle.desc}>ingrese su correo estudiantil y contraseña</Text>

                    <View style={registerStyle.card}>
                        <TextInput  
                        placeholder='codigo estudiantil' 
                        placeholderTextColor="slategray" 
                        value={codigo} 
                        onChangeText={setCodigo}
                        style={registerStyle.input} 
                        />
                    
                        <TextInput  
                        placeholder='contraseña' 
                        placeholderTextColor="slategray" 
                        value={contraseña} 
                        onChangeText={setContraseña}
                        style={registerStyle.input} 
                        />

                        <TouchableOpacity onPress={saveNote} style={registerStyle.button}>
                            <Text style={registerStyle.buttonText}>Ingresar</Text>
                        </TouchableOpacity>
                    </View>
                </View>
            </ScrollView>
        )
}

