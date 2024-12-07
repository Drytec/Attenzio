import { Text, View, TouchableOpacity } from "react-native";
import { homeStyles } from "../styles/homeStyle";

export default function Home({navigation}){
    return(
        <View style={homeStyles.main}> 
            <Text style={homeStyles.tittle}>
        Atten
        <Text style={homeStyles.highlight}>zio</Text>
      </Text>
            <Text style={homeStyles.desc}> inicia sesion o crea una cuenta para ingresar </Text>
            <TouchableOpacity onPress={()=>navigation.navigate('Log')} style={homeStyles.buttonAdd}>
                <Text style={homeStyles.textbuttonadd}>iniciar sesion</Text>
            </TouchableOpacity> 
            <TouchableOpacity onPress={()=>navigation.navigate('Register')} style={homeStyles.buttonAdd}>
                <Text style={homeStyles.textbuttonadd}>registrate</Text>
            </TouchableOpacity>  
        </View>
    )
}

