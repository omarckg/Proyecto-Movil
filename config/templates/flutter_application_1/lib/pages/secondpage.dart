
import 'package:flutter/material.dart';
import 'package:flutter_application_1/forms/form_user.dart';
import 'package:provider/provider.dart';



class SecondPage extends StatelessWidget {
  const SecondPage({super.key});

  @override
  Widget build(BuildContext context) {
    final formuserprovider = Provider.of<FormUser>(context);
    return Scaffold(
      appBar: AppBar(
        title: const Text('Second Page'),
      ),
      body: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.center,
          children: [

            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Text('Nombre; ${formuserprovider.nombre} ',
              style: TextStyle(
                fontSize: 20,
              ),),
            ), 
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Text('Apellido; ${formuserprovider.apellido} ',
              style: TextStyle(
                fontSize: 20,
              ),),
            ), 
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Text('Edad; ${formuserprovider.edad} ',
              style: TextStyle(
                fontSize: 20,
              ),),
            ), 
          ],
        ),
      ),
    );
  }
}