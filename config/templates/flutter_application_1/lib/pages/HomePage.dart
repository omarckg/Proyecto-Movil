import 'package:flutter/material.dart';
import 'package:flutter_application_1/pages/details.dart';

class WelcomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Colors.blue, Colors.purple], // Colores del fondo
          ),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              Icons.food_bank,
              size: 100,
              color: Colors.white,
            ),
            SizedBox(height: 20),
            Text(
              'Bienvenido a\nBanco de Alimentos',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 32,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
            SizedBox(height: 10),
            Text(
              'Luchando contra el hambre y la necesidad en nuestra comunidad',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 16,
                color: Colors.white,
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.pushReplacement(
                  context,
                  MaterialPageRoute(builder: (context) => HomeScreen()),
                );
              },
              style: ElevatedButton.styleFrom(
                primary: Colors.orange,
              ),
              child: Text('Empezar'),
            ),
          ],
        ),
      ),
    );
  }
}

class HomeScreen extends StatelessWidget {
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Banco de alimentos',style: TextStyle(
                fontSize: 16,
                color: Colors.white),
        ),     
        backgroundColor: Colors.orange,
        actions: [
          IconButton(
            icon: Icon(Icons.home),
            onPressed: () {
              Navigator.pushReplacement(
                context,
                MaterialPageRoute(builder: (context) => WelcomeScreen()),
              );
            },
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: GridView.count(
          crossAxisCount: 2,
          crossAxisSpacing: 16.0,
          mainAxisSpacing: 16.0,
          children: [
            buildCard(context, 'Bodega', Icons.store),
            buildCard(context, 'Categoría', Icons.category),
            buildCard(context, 'Producto', Icons.shopping_cart),
            buildCard(context, 'Usuario', Icons.person),
            buildCard(context, 'Vehículos', Icons.directions_car),
            buildCard(context, 'Conductor', Icons.person_pin),
            buildCard(context, 'Formulario', Icons.assignment),
          ],
        ),
      ),
    );
  }

  Widget buildCard(BuildContext context, String title, IconData icon) {
    return Card(
      elevation: 5,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(15.0),
      ),
      child: InkWell(
        onTap: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => DetailScreen(title)),
          );
        },
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon,
                size: 50, color: Colors.blue.shade400),
            SizedBox(height: 10),
            Text(
              title,
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
                color: Colors.black
              ),
            ),
          ],
        ),
      ),
    );
  }
}


