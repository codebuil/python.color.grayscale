from PIL import Image

def convert_to_grayscale(input_file, output_file):
    try:
        # Abra a imagem BMP de 24 bits
        image = Image.open(input_file)

        # Converta a imagem para tons de cinza
        grayscale_image = image.convert("L")

        # Salve a imagem em tons de cinza como BMP
        grayscale_image.save(output_file)

        print(f"Conversão concluída. Imagem em tons de cinza salva em '{output_file}'.")

    except FileNotFoundError:
        print(f"Arquivo '{input_file}' não encontrado.")


input_file = "my.bmp"   # Substitua pelo nome do seu arquivo BMP de entrada
output_file = "output.bmp" # Substitua pelo nome do arquivo BMP de saída em tons de cinza
convert_to_grayscale(input_file, output_file)
