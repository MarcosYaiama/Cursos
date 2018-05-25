<?php
if(isset($_POST['1ON']))
{
  exec('gpio -1 mode 7 out');
  exec('gpio -1 write 7 1');
}
if(isset($_POST['1OFF']))
{
  exec('gpio -1 mode 7 out');
  exec('gpio -1 write 7 0');
}
if(isset($_POST['2ON']))
{
  exec('gpio -1 mode 11 out');
  exec('gpio -1 write 11 1');
}
if(isset($_POST['2OFF']))
{
  exec('gpio -1 mode 11 out');
  exec('gpio -1 write 11 0');
}
if(isset($_POST['3ON']))
{
  exec('gpio -1 mode 12 out');
  exec('gpio -1 write 12 1');
}
if(isset($_POST['3OFF']))
{
  exec('gpio -1 mode 12 out');
  exec('gpio -1 write 12 0');
}
if(isset($_POST['4ON']))
{
  exec('gpio -1 mode 13 out');
  exec('gpio -1 write 13 1');
}
if(isset($_POST['4OFF']))
{
  exec('gpio -1 mode 13 out');
  exec('gpio -1 write 13 0');
}
if(isset($_POST['5ON']))
{
  exec('gpio -1 mode 15 out');
  exec('gpio -1 write 15 1');
}
if(isset($_POST['5OFF']))
{
  exec('gpio -1 mode 15 out');
  exec('gpio -1 write 15 0');
}
if(isset($_POST['6ON']))
{
  exec('gpio -1 mode 16 out');
  exec('gpio -1 write 16 1');
}
if(isset($_POST['6OFF']))
{
  exec('gpio -1 mode 16 out');
  exec('gpio -1 write 16 0');
}
?>

<html>
  <body>
    <form method="POST">
      <table style="width: 20%; text-align: left; margin-left: auto; margin-right: auto;">
        <tr>
          <td style="text-align: center;">DEVICE 1</td>
          <td style="text-align: center;"><button name="1ON">ON</button></td>
          <td style="text-align: center;"><button name="1OFF">OFF</button></td>
        </tr>
        <tr>
          <td style="text-align: center;">DEVICE 2</td>
          <td style="text-align: center;"><button name="2ON">ON</button></td>
          <td style="text-align: center;"><button name="2OFF">OFF</button></td>
        </tr>
        <tr>
          <td style="text-align: center;">DEVICE 3</td>
          <td style="text-align: center;"><button name="3ON">ON</button></td>
          <td style="text-align: center;"><button name="3OFF">OFF</button></td>
        </tr>
        <tr>
          <td style="text-align: center;">DEVICE 4</td>
          <td style="text-align: center;"><button name="4ON">ON</button></td>
          <td style="text-align: center;"><button name="4OFF">OFF</button></td>
        </tr>
        <tr>
          <td style="text-align: center;">DEVICE 5</td>
          <td style="text-align: center;"><button name="5ON">ON</button></td>
          <td style="text-align: center;"><button name="5OFF">OFF</button></td>
        </tr>
        <tr>
          <td style="text-align: center;">DEVICE 6</td>
          <td style="text-align: center;"><button name="6ON">ON</button></td>
          <td style="text-align: center;"><button name="6OFF">OFF</button></td>
        </tr>
      </table>
    </form>
  </body>
</html>
