import { Text, View, ScrollView, TextInput, TouchableOpacity, Alert, ImageBackground, Image } from "react-native";
import { useState } from "react";
import * as ImagePicker from 'expo-image-picker'; // Cambia a la importación correcta
import { registerStyle } from "../styles/registerStyle";

export default function Register({ navigation }) {
    const [codigo, setCodigo] = useState('');
    const [contraseña, setContraseña] = useState('');
    const [ccontraseña, setcContraseña] = useState('');
    const [nombre, setNombre] = useState('');
    const [cel, setCel] = useState('');
    const [correo, setCorreo] = useState('');
    const [foto, setFoto] = useState(null); // Estado para guardar la foto
    const [showContraseña, setShowContraseña] = useState(false);
    const [showCContraseña, setShowCContraseña] = useState(false);

    const saveNote = () => {
        if (!codigo.trim() || !contraseña.trim() || !nombre.trim() || !cel.trim() || !correo.trim()) {
            Alert.alert('Error', 'Por favor, complete todos los campos antes de continuar.');
            return;
        }
        if (contraseña !== ccontraseña) {
            Alert.alert('Error', 'Las contraseñas no coinciden. Por favor, intente de nuevo.');
            return;
        }

        Alert.alert('Aviso', 'Has sido registrado correctamente.');
        navigation.navigate('Log');
    };

    const cargarDesdeGaleria = async () => {
        const result = await ImagePicker.launchImageLibraryAsync({
            mediaTypes: ImagePicker.MediaTypeOptions.Images,
            allowsEditing: true,
            quality: 1,
        });

        if (!result.canceled) {
            setFoto(result.assets[0].uri); // Guarda la URI de la imagen seleccionada
        } else {
            Alert.alert('Aviso', 'No se seleccionó ninguna imagen.');
        }
    };

    return (
        <ScrollView contentContainerStyle={registerStyle.scrollContainer}>
            <ImageBackground 
                source={require('../assets/fondo.png')} 
                style={registerStyle.background}
            >
                <View style={registerStyle.main}>
                    <Text style={registerStyle.tittle}>
                        Registr<Text style={registerStyle.highlight}>arse</Text>
                    </Text>

                    <View style={registerStyle.card}>
                        <Text style={registerStyle.desc}>Ingrese su código estudiantil:</Text>
                        <TextInput  
                            placeholder='Código estudiantil' 
                            placeholderTextColor="slategray" 
                            value={codigo} 
                            onChangeText={setCodigo}
                            style={registerStyle.input} 
                        />

                        <Text>Ingrese su nombre y apellidos:</Text>
                        <TextInput  
                            placeholder='Nombre' 
                            placeholderTextColor="slategray" 
                            value={nombre} 
                            onChangeText={setNombre}
                            style={registerStyle.input} 
                        />

                        <Text>Número de celular:</Text>
                        <TextInput  
                            placeholder='Número' 
                            placeholderTextColor="slategray" 
                            value={cel} 
                            onChangeText={setCel}
                            style={registerStyle.input} 
                        />

                        <Text>Correo institucional:</Text>
                        <TextInput  
                            placeholder='Correo' 
                            placeholderTextColor="slategray" 
                            value={correo} 
                            onChangeText={setCorreo}
                            style={registerStyle.input} 
                        />

                        <Text>Contraseña:</Text>
                        <View style={registerStyle.passwordContainer}>
                            <TextInput  
                                placeholder='Contraseña' 
                                placeholderTextColor="slategray" 
                                value={contraseña} 
                                onChangeText={setContraseña}
                                secureTextEntry={!showContraseña} 
                                style={[registerStyle.input, { flex: 1 }]} 
                            />
                            <TouchableOpacity onPress={() => setShowContraseña(!showContraseña)}>
                                <Text style={registerStyle.show}>{showContraseña ? 'Ocultar' : 'Mostrar'}</Text>
                            </TouchableOpacity>
                        </View>

                        <Text>Confirma tu contraseña:</Text>
                        <View style={registerStyle.passwordContainer}>
                            <TextInput  
                                placeholder='Confirmar contraseña' 
                                placeholderTextColor="slategray" 
                                value={ccontraseña} 
                                onChangeText={setcContraseña}
                                secureTextEntry={!showCContraseña}
                                style={[registerStyle.input, { flex: 1 }]} 
                            />
                            <TouchableOpacity onPress={() => setShowCContraseña(!showCContraseña)}>
                                <Text style={registerStyle.show}>{showCContraseña ? 'Ocultar' : 'Mostrar'}</Text>
                            </TouchableOpacity>
                        </View>

                        <Text style={registerStyle.desc}>Suba una captura de su registro académico tocando el icono:</Text>
                        
                        {foto ? (
                            <Image source={{ uri: foto }} style={registerStyle.imagePreview} />
                        ) : (
                            <TouchableOpacity onPress={cargarDesdeGaleria}>
                                <Image source={require('../assets/imageicon.png')} style={registerStyle.imagePreview} />
                            </TouchableOpacity>
                        )}

                        <TouchableOpacity onPress={saveNote} style={registerStyle.button}>
                            <Text style={registerStyle.buttonText}>Registrarse</Text>
                        </TouchableOpacity>
                    </View>
                </View>
            </ImageBackground>
        </ScrollView>
    );
}

