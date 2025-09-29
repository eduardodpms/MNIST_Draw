from google.colab import output as op
from IPython.display import HTML
from base64 import b64decode
from PIL import Image
import io
import os



def draw(output='drawing.png', w=256, h=256, line_width=10, color="white", bg_color="black", resize=True, gray=True, canvas_fade=False):
  real_filename = os.path.realpath(output)
  canvas_fade = 1 if canvas_fade else 0 # Translating Python boolean to JS boolean

  canvas_html = f"""
    <canvas width={w} height={h}></canvas>

    <div class="slidecontainer">
      &nbsp&nbsp&nbsp&nbsp Traço: &nbsp
      <label for="lineWidth" id="lineWidthLabel">{line_width}px </label>
      <input type="range" min="1" max="50" value={line_width} class="slider" id="lineWidth">
    </div>

    <div style="div_align: center">
      &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
      <button id="save">Salvar</button>
      <button id="reset">Limpar</button>
      <button id="exit">Sair</button>
    </div>

    <script>
      var canvas = document.querySelector('canvas')
      var ctx = canvas.getContext('2d')

      ctx.lineWidth = {line_width}
      ctx.fillStyle = "{bg_color}";
      ctx.strokeStyle = "{color}";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      var slider = document.getElementById("lineWidth");

      slider.oninput = function() {{
        ctx.lineWidth = this.value;
        lineWidthLabel.innerHTML = `${{this.value}}px`
      }}
      
      var save_button = document.querySelector('#save')
      var clear_button = document.querySelector('#reset')
      var exit_button = document.querySelector('#exit')

      var mouse = {{x: 0, y: 0}}

      canvas.addEventListener('mousemove', function(e) {{
        mouse.x = e.pageX - this.offsetLeft
        mouse.y = e.pageY - this.offsetTop
      }})

      canvas.onmousedown = ()=>{{
        ctx.beginPath()
        ctx.moveTo(mouse.x, mouse.y)
        canvas.addEventListener('mousemove', onPaint)
      }}

      canvas.onmouseup = ()=>{{
        canvas.removeEventListener('mousemove', onPaint)
      }}

      var onPaint = ()=>{{
        ctx.lineTo(mouse.x, mouse.y)
        ctx.stroke()
      }}
      
      clear_button.onclick = ()=>{{
        console.log('Clearing Screen')
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillRect(0, 0, canvas.width, canvas.height);
      }}

      var data = new Promise(resolve=>{{
        save_button.onclick = ()=>{{
          var imgData = canvas.toDataURL('image/png');
          if ({canvas_fade}) canvas.style.display = "none";
          resolve(imgData)
        }}

        exit_button.onclick = ()=>{{
          if ({canvas_fade}) canvas.style.display = "none";
          resolve()
        }}
      }})
    </script>
  """

  display(HTML(canvas_html))
  data = op.eval_js("data")

  if data:
    print(f"\nSalvo em: {real_filename}")
    binary = b64decode(data.split(',')[1])
    img = Image.open(io.BytesIO(binary))

    if resize:
      img = img.resize((28, 28), Image.Resampling.LANCZOS) # Resize to 28x28

    if gray:
      img = img.convert('L') # Ensure Gray scale
        
    img.save(output)

  else:
    print(f"\nVocê saiu do desenho.")