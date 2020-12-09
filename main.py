def web_page():
  
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="icon" href="data:,">
  <style>body{text-align: center;font-family:"Trebuchet MS",Arial;margin-left:auto;margin-right:auto;}
  .slider{width: 300px;}</style><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script></head>
  <body><h1>Robotic Arm</h1><h6>Ormolgud Gonzalez Cardona</h6><h6>Juan Carlos Salazar Munoz</h6>
  <p>Middle:<span id="servoPosMiddle"></span></p><input type="range" min="0" max="180" class="slider" id="servoSliderMiddle" onchange="fMiddle(this.value)"/>
  <p>Left:<span id="servoPosLeft"></span></p><input type="range" min="0" max="180" class="slider" id="servoSliderLeft" onchange="fLeft(this.value)"/>
  <p>Right:<span id="servoPosRight"></span></p><input type="range" min="0" max="180" class="slider" id="servoSliderRight" onchange="fRight(this.value)"/>
  <p>Claw:<span id="servoPosClaw"></span></p><input type="range" min="0" max="180" class="slider" id="servoSliderClaw" onchange="fClaw(this.value)"/>
  <h6>Arquitectura de Hardware</h6><h6>Jose Leon Henao Rios</h6><h6>Politecnico Colombiano JIC</h6>
  <script>
  var sliderMiddle = document.getElementById("servoSliderMiddle");
  var servoPMiddle = document.getElementById("servoPosMiddle");
  servoPMiddle.innerHTML = sliderMiddle.value;
  sliderMiddle.oninput = function(){
  sliderMiddle.value = this.value;
  servoPMiddle.innerHTML = this.value;
  }
  var sliderLeft = document.getElementById("servoSliderLeft");
  var servoPLeft = document.getElementById("servoPosLeft");
  servoPLeft.innerHTML = sliderLeft.value;
  sliderLeft.oninput = function() {
  sliderLeft.value = this.value;
  servoPLeft.innerHTML = this.value;
  }  
  var sliderRight = document.getElementById("servoSliderRight");
  var servoPRight = document.getElementById("servoPosRight");
  servoPRight.innerHTML = sliderRight.value;
  sliderRight.oninput = function() {
  sliderRight.value = this.value;
  servoPRight.innerHTML = this.value;
  }
  var sliderClaw = document.getElementById("servoSliderClaw");
  var servoPClaw = document.getElementById("servoPosClaw");
  servoPClaw.innerHTML = sliderClaw.value;
  sliderClaw.oninput = function() {
  sliderClaw.value = this.value;
  servoPClaw.innerHTML = this.value;
  }
  $.ajaxSetup({timeout:1000});
  function fMiddle(pos) {
  $.get("/?valueMiddle=" + pos + "&");
  {Connection: close};}
  function fLeft(pos) {
  $.get("/?valueLeft=" + pos + "&");
  {Connection: close};}
  function fRight(pos) {
  $.get("/?valueRight=" + pos + "&");
  {Connection: close};}
  function fClaw(pos) {
  $.get("/?valueClaw=" + pos + "&");
  {Connection: close};}
  </script></body></html>"""
  return html
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  if "valueMiddle" in request:
    valueMiddle = int(request[request.index("=") + 1:request.index("&")]) * (100 / 180) + 20
    print("valueMiddle " + str(valueMiddle))
    pwmMiddle.duty(int(valueMiddle))
  elif "valueLeft" in request:
    valueLeft = int(request[request.index("=") + 1:request.index("&")]) * (100 / 180) + 20
    print("valueLeft " + str(valueLeft))
    pwmLeft.duty(int(valueLeft))
  elif "valueRight" in request:
    valueRight = (int(request[request.index("=") + 1:request.index("&")]) * (11 / 18) + 70) * (100 / 180) + 20
    print("valueRight " + str(valueRight))
    pwmRight.duty(int(valueRight))
  elif "valueClaw" in request:
    valueClaw = (int(request[request.index("=") + 1:request.index("&")]) * (1 / 3) + 70) * (100 / 180) + 20
    print("valueClaw " + str(valueClaw))
    pwmClaw.duty(int(valueClaw))
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
