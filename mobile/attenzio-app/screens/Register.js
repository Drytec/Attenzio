import { Text, View, ScrollView, TextInput, TouchableOpacity } from "react-native";
import { useState } from "react";

export default function Register(){
    const [titulo, setTitulo] = useState('')
    const [descorta, setDescorta] = useState('')
    const [fecha, setFecha] = useState('')
    const [descripcion, setDescripcion] = useState('')
        return(
            <ScrollView>
                <View>
                    <Text>Crear nota</Text>

                    <View>
                        <TextInput  
                        placeholder='titulo' 
                        placeholderTextColor="slategray" 
                        value={titulo} 
                        onChangeText={setTitulo} 
                        />
                    </View>
                </View>
            </ScrollView>
        )
}

