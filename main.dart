import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'led',
      theme: ThemeData(
        primarySwatch: Colors.orange,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(title: 'Led'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

Future<http.Response> postData(String lightState) {
  return http.post(
    'http://YOUR.RPI.IP.ADRESS:8000',                       //SET UP IP 
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{
      'lightState': lightState,
    }),
  );
}

class _MyHomePageState extends State<MyHomePage> {
  String lightState = '';
  int count = 0;
  TextEditingController ledConstroller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text(widget.title),
        ),
        body: Center(
            child: Column(
          children: [
            Spacer(),
            RaisedButton.icon(
              icon: Icon(Icons.lightbulb_outline),
              label: Text('tap to make the magic'),
              onPressed: () {
                setState(() {
                  if (count == 0) {
                    this.lightState = 'on';
                    count++;
                  } else {
                    this.lightState = 'off';
                    count = 0;
                  }
                  ledConstroller.text = lightState;
                  var data = postData(ledConstroller.text);
                });
              },
            ),
            RaisedButton.icon(
              icon: Icon(Icons.power_settings_new),
              label: Text('power off'),
              onPressed: () {
                setState(() {
                  this.lightState = '0';
                  ledConstroller.text = lightState;
                  var data = postData(ledConstroller.text);
                });
              },
            ),
            Spacer(),
          ],
        )),
        backgroundColor: Colors.deepOrange);
  }
}
