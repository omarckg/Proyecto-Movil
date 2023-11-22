import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl = 'http://omarfuentes.pythonanywhere.com';

  Future<void> fetchData(String ruta) async {
    try {
      final response = await http.get(Uri.parse('$baseUrl/$ruta'));
      print('Respuesta $ruta: ${response.body}');
    } catch (error) {
      print('Error: $error');
    }
  }
}
