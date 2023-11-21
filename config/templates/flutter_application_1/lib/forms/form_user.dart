import 'package:flutter/material.dart';

class FormUser extends ChangeNotifier {

  GlobalKey<FormState> formkey = GlobalKey<FormState>();
  

  String nombre = "";
  String apellido = "";
  String edad = "";

}