import { StatusBar } from "expo-status-bar";
import {
  StyleSheet,
  Text,
  View,
  ScrollViewBase,
  ScrollView,
  SafeAreaView,
} from "react-native";

const scrollItems = Array.from({ length: 400 }, () =>
  Math.floor(Math.random() * 40)
);

export default function App() {
  return (
    <>
      {/* <View style={styles.container}>
        <Text>Open up App.js to start working on your app!</Text>
        <StatusBar style="auto" />
      </View> */}
      <SafeAreaView>
        <div>
          {scrollItems.map(x => {
            return <Text>{String(x)} {'\n'}</Text>;
          })
          }
        </div>
      </SafeAreaView>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
