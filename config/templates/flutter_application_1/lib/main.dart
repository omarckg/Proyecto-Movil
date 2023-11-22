import 'package:flutter/material.dart';
import 'package:flutter_application_1/pages/HomePage.dart';


void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark().copyWith(
        primaryColor: Colors.blue,
        colorScheme:
            ColorScheme.fromSwatch().copyWith(secondary: Colors.blueAccent),
      ),
      home: WelcomeScreen(),
    );
  }
}

