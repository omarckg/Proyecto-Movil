import 'package:flutter/material.dart';
import 'package:flutter_application_1/Providers/Provider.dart';
import 'package:flutter_application_1/models/ModeloBodega.dart';

import 'package:flutter_application_1/pages/HomePage.dart';

class DetailScreen extends StatefulWidget {
  final String title;

  DetailScreen(this.title);
  
  State<DetailScreen> createState() => _DetailScreenState();
}
 
class _DetailScreenState extends State<DetailScreen> {
  final welcomeProvider = WelcomeProvider(); // Instancia del Provider
  final ScrollController _scrollController = ScrollController();
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    _scrollController.addListener(_scrollListener);
    _loadData();
  }

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }

  void _scrollListener() {
    if (_scrollController.position.pixels ==
        _scrollController.position.maxScrollExtent) {
      _loadData();
    }
  }

  Future<void> _loadData() async {
    if (!_isLoading) {
      setState(() {
        _isLoading = true;
      });

      await welcomeProvider
          .fetchData(); // Llamada al método fetchData para cargar datos

      setState(() {
        _isLoading = false;
      });
    }
  }
  
  
  
  
  
  
  
  Widget build(BuildContext context) {
   final welcomeProvider = WelcomeProvider(); // Instancia del Provider

    return Scaffold(
      appBar: AppBar(title: const Text('Welcome Info')),
      body: FutureBuilder<void>(
        future: welcomeProvider
            .fetchData(), // Llamada al método fetchData para cargar datos
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else {
            return ListView.builder(
              itemCount: welcomeProvider.welcomeList.length,
              itemBuilder: (context, index) {
                final welcome = welcomeProvider.welcomeList[index];
                return Card(
                  elevation: 3,
                  margin: EdgeInsets.symmetric(vertical: 8, horizontal: 16),
                  color: Colors.white, // Cambia el color de fondo
                  shape: RoundedRectangleBorder(
                    borderRadius:
                        BorderRadius.circular(8), // Agrega bordes redondeados
                    // Puedes agregar más personalización aquí
                  ),
                  child: ListTile(
                    title: Text(welcome.nombre as String ),
                    subtitle: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text('Organizacion: ${welcome.nombre}'),
                        
                        // Agrega más campos aquí...
                      ],
                    ),
                    
                  ),
                );
              },
            );
          }
        },
      ),
    );
  }

  



}
