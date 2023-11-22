
import 'package:flutter_application_1/models/ModeloBodega.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

 // Asegúrate de importar correctamente el modelo

// Clase que provee la funcionalidad para obtener datos de la API
class WelcomeProvider {
  final String apiUrl =
      'http://omarfuentes.pythonanywhere.com/api/Bodega'; // URL de la API

  List<Welcome> _welcomeList = []; // Lista para almacenar los datos obtenidos

  List<Welcome> get welcomeList =>
      _welcomeList; // Getter para obtener la lista de datos

  // Método para obtener y cargar los datos de la API
  Future<void> fetchData() async {
    try {
      final response = await http
          .get(Uri.parse(apiUrl)); // Hace una solicitud GET a la URL de la API

      if (response.statusCode == 200) {
        final jsonData =
            json.decode(response.body); // Decodifica la respuesta JSON obtenida
        _welcomeList = List<Welcome>.from(jsonData.map((x) => Welcome.fromJson(
            x))); // Convierte los datos JSON en objetos Welcome y los agrega a la lista
      } else {
        throw Exception(
            'Failed to load data from API'); // Lanza una excepción si la solicitud no fue exitosa
      }
    } catch (e) {
      throw Exception(
          'Failed to load data: $e'); // Lanza una excepción si ocurre un error durante la solicitud
    }
  }
}
