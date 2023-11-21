import 'package:flutter/material.dart';
import 'package:flutter_application_1/pages/homepage.dart';
import 'package:flutter_application_1/pages/secondpage.dart';
import 'package:provider/provider.dart';

import 'forms/form_user.dart';


void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (context) =>  FormUser(),),
        
      ],
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        //home: 
        initialRoute: 'home',
        routes: {
          'home'    :(_) => HomePage(),
          'second' :(_) => SecondPage(),
        },
      ),
    );
  }
}

