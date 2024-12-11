import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import 'react-native-gesture-handler';
import { createStackNavigator } from '@react-navigation/stack';
import { NavigationContainer } from '@react-navigation/native';
import Home from './screens/Home';
import Register from './screens/Register';
import Log from './screens/Log';
import Userqr from './screens/Userqr';
import Classqu from './screens/Classqu';
import RegisterPh from './screens/RegisterPh';

export default function App() {
  const Stack = createStackNavigator();
  function MyStack() {
    return(
      <Stack.Navigator screenOptions={{headerShown:false}}>
        <Stack.Screen name="Home" component={Home} />
        <Stack.Screen name="Register" component={Register} />
        <Stack.Screen name="Log" component={Log} />
        <Stack.Screen name="Userqr" component={Userqr} />
        <Stack.Screen name="Classqu" component={Classqu} />
        <Stack.Screen name="Registerph" component={RegisterPh} />
      </Stack.Navigator>
    );
  } 
  return (
    <NavigationContainer>
      <MyStack />
    </NavigationContainer>
  );
}



