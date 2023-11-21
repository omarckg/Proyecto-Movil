
import 'package:flutter/material.dart';
import 'package:flutter_application_1/forms/form_user.dart';
import 'package:flutter_application_1/widgets/inputdecorationcustom.dart';
import 'package:provider/provider.dart';


class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    final formuserprovider = Provider.of<FormUser>(context);
    return Scaffold(
      appBar: AppBar(
        title: const Text('Codeveloper'),
      ),
      body: SingleChildScrollView(
        child: Container(
          margin: EdgeInsets.only(
            top: 30,
            left: 20,
            right: 20,
          ),
          child: Form(
            key: formuserprovider.formkey,
            autovalidateMode: AutovalidateMode.onUserInteraction,
            child: Column(
              children: [
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: TextFormField(
                    keyboardType: TextInputType.text,
                    onChanged: (value) {
                      formuserprovider.nombre = value.toString();
                    },
                    validator: (value) {
                      if(value!.isEmpty) return 'Escriba su nombre';
                    },
                    decoration: InputDecorationCustom.getInputDecoration(
                      labeltext: 'Nombre',
                      hintext: 'nombre',
                      prefixicon: Icons.person,
                    ),
                  ),
                ),

                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: TextFormField(
                    keyboardType: TextInputType.text,
                    onChanged: (value) {
                      formuserprovider.apellido = value.toString();
                    },
                    validator: (value) {
                      if(value!.isEmpty) return 'Escriba su apellido';
                    },
                    decoration: InputDecorationCustom.getInputDecoration(
                      labeltext: 'Apellido',
                      hintext: 'apellido',
                      prefixicon: Icons.person,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: TextFormField(
                    keyboardType: TextInputType.number,
                    onChanged: (value) {
                      formuserprovider.edad = value.toString();
                    },
                    validator: (value) {
                      if(value!.isEmpty) return 'Escriba su nombre';
                    },
                    decoration: InputDecorationCustom.getInputDecoration(
                      labeltext: 'Edad',
                      hintext: 'edad',
                      prefixicon: Icons.calendar_month,
                    ),
                  ),
                ),
          
                Container(
                  height: 60,
                  width: 140,
                  decoration: BoxDecoration(
                    color: Colors.purpleAccent,
                    borderRadius: BorderRadius.circular(30),
                  ),
                  child: MaterialButton(
                    child: const Text(
                      'Enviar',
                      style: TextStyle(
                        fontSize: 20,
                      ),
                    ),
                    onPressed: () {

                      FocusScope.of(context).unfocus();
                      if(formuserprovider.formkey.currentState!.validate()){
                        //print('correcto');
                        Navigator.pushNamed(context, 'second');
                      }else{
                        ScaffoldMessenger.of(context).showSnackBar(
                          SnackBar(content: Text('Falta información !!')),
                        );
                      }

                    },
                  ),
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
