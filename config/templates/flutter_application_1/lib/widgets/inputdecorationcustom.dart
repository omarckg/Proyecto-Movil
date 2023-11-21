import 'package:flutter/material.dart';

class InputDecorationCustom {

  static InputDecoration getInputDecoration ({

    required String labeltext, 
    required String hintext, 
    IconData? prefixicon,

  }){
    return InputDecoration(
      enabledBorder: const OutlineInputBorder(
        borderSide: BorderSide(
          color: Colors.blueAccent,
          style: BorderStyle.solid,
        )
      ), 
      focusedBorder: const  OutlineInputBorder(
        borderSide: BorderSide(
          color: Colors.blueAccent,
          style: BorderStyle.solid,
        )
      ),
      labelText: labeltext, 
      hintText: hintext, 
      prefixIcon: prefixicon != null ? Icon(prefixicon, 
        color: Colors.purpleAccent,
      ) : null 
    );
  }


}