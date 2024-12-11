import { Text, View, ScrollView, TextInput, TouchableOpacity, Alert, ImageBackground } from "react-native";
import { useState } from "react";
import { logStyle } from "../styles/logStyle";

export default function Log({navigation}){
    const [codigo, setCodigo] = useState('')
    const [contraseña, setContraseña] = useState('')
    const [showContraseña, setShowContraseña] = useState(false);

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
                <ImageBackground source={require('../assets/fondo.png')} 
                style={logStyle.background}>

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
                    
                    <Text>Contraseña:</Text>
                        <View style={logStyle.passwordContainer}>
                            <TextInput  
                                placeholder='Contraseña' 
                                placeholderTextColor="slategray" 
                                value={contraseña} 
                                onChangeText={setContraseña}
                                secureTextEntry={!showContraseña} 
                                style={[logStyle.input, { flex: 1 }]} 
                            />
                            <TouchableOpacity onPress={() => setShowContraseña(!showContraseña)}>
                                <Text style={logStyle.show}>{showContraseña ? 'Ocultar' : 'Mostrar'}</Text>
                            </TouchableOpacity>
                        </View>

                        <TouchableOpacity onPress={saveNote} style={logStyle.button}>
                            <Text style={logStyle.buttonText}>Ingresar</Text>
                        </TouchableOpacity>
                    </View>
                </View>
                </ImageBackground>
            </ScrollView>
        )
}

