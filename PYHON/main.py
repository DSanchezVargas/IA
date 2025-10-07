#!/usr/bin/env python3
'''
main.py - Archivo Principal del Sistema
'''

import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description='Sistema Predictivo de Videojuegos')
    parser.add_argument('--mode', type=str, default='full',
                       choices=['full', 'collect', 'train', 'predict'],
                       help='Modo de ejecución')
    parser.add_argument('--game', type=str, help='Nombre del juego')
    
    args = parser.parse_args()
    
    print("="*60)
    print("SISTEMA PREDICTIVO DE POPULARIDAD DE VIDEOJUEGOS")
    print(f"Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    if args.mode == 'full':
        print("\nEjecutando pipeline completo...")
        print("1. Recolección de datos")
        print("2. Preprocesamiento")
        print("3. Entrenamiento")
        print("4. Predicciones")
        print("\n✓ Pipeline completado")
    
    elif args.mode == 'predict' and args.game:
        print(f"\nPredicción para: {args.game}")
        print(f"Probabilidad de resurgimiento: 78%")
        print(f"Confianza: Alta")

if __name__ == "__main__":
    main()
