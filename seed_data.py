"""
Script para generar datos iniciales en la base de datos
Ejecutar: python seed_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mivivienda_project.config.settings')
django.setup()

from django.contrib.auth.models import User, Group
from mivivienda_project.apps.financial.models import EntidadFinanciera, BonoBuenPagador
from mivivienda_project.apps.business.models import Proyecto, Inmueble, Cliente
from datetime import datetime
from decimal import Decimal


def crear_grupos_y_permisos():
    """Crea los grupos de usuarios (ADMIN, VENDEDOR)"""
    print("📋 Creando grupos...")
    
    grupos = ['ADMIN', 'VENDEDOR']
    for grupo_nombre in grupos:
        grupo, created = Group.objects.get_or_create(name=grupo_nombre)
        if created:
            print(f"  ✓ Grupo '{grupo_nombre}' creado")
        else:
            print(f"  - Grupo '{grupo_nombre}' ya existe")
    
    return Group.objects.filter(name__in=grupos)


def crear_usuarios(grupos):
    """Crea usuarios en auth_user para login"""
    print("\n👥 Creando usuarios...")
    
    usuarios_data = [
        {
            'username': 'admin',
            'email': 'admin@mivivienda.com',
            'password': 'Admin123456',
            'first_name': 'Administrador',
            'last_name': 'Sistema',
            'grupo': 'ADMIN'
        },
        {
            'username': 'juan_perez',
            'email': 'juan.perez@mivivienda.com',
            'password': 'Juan123456',
            'first_name': 'Juan',
            'last_name': 'Pérez',
            'grupo': 'VENDEDOR'
        },
        {
            'username': 'maria_garcia',
            'email': 'maria.garcia@mivivienda.com',
            'password': 'Maria123456',
            'first_name': 'María',
            'last_name': 'García',
            'grupo': 'VENDEDOR'
        },
        {
            'username': 'carlos_lopez',
            'email': 'carlos.lopez@mivivienda.com',
            'password': 'Carlos123456',
            'first_name': 'Carlos',
            'last_name': 'López',
            'grupo': 'VENDEDOR'
        }
    ]
    
    usuarios_creados = []
    for datos in usuarios_data:
        user, created = User.objects.get_or_create(
            username=datos['username'],
            defaults={
                'email': datos['email'],
                'first_name': datos['first_name'],
                'last_name': datos['last_name'],
                'is_staff': datos['grupo'] == 'ADMIN',
                'is_superuser': datos['grupo'] == 'ADMIN'
            }
        )
        
        user.set_password(datos['password'])
        user.save()
        
        grupo = grupos.get(name=datos['grupo'])
        user.groups.add(grupo)
        
        if created:
            print(f"  ✓ Usuario '{datos['email']}' ({datos['grupo']}) creado")
        else:
            print(f"  - Usuario '{datos['email']}' ya existe")
        
        usuarios_creados.append(user)
    
    return usuarios_creados


def crear_entidades_financieras():
    """Crea las 6 entidades financieras principales"""
    print("\n🏦 Creando entidades financieras...")
    entidades_data = [
        {
            'nombre': 'Banco de Crédito del Perú',
            'tasa_desgravamen': Decimal('0.000100'),
            'tasa_riesgo': Decimal('0.000150'),
            'comision_mensual': Decimal('15.00'),
            'tasa_cok': Decimal('0.12'),
            'tasa_ea_referencial': Decimal('0.08'),
        },
        {
            'nombre': 'Scotiabank Perú S.A.A.',
            'tasa_desgravamen': Decimal('0.000105'),
            'tasa_riesgo': Decimal('0.000155'),
            'comision_mensual': Decimal('14.50'),
            'tasa_cok': Decimal('0.12'),
            'tasa_ea_referencial': Decimal('0.0825'),
        },
        {
            'nombre': 'Banco Interamericano de Finanzas',
            'tasa_desgravamen': Decimal('0.000110'),
            'tasa_riesgo': Decimal('0.000160'),
            'comision_mensual': Decimal('16.00'),
            'tasa_cok': Decimal('0.125'),
            'tasa_ea_referencial': Decimal('0.085'),
        },
        {
            'nombre': 'BBVA Banco Continental',
            'tasa_desgravamen': Decimal('0.000095'),
            'tasa_riesgo': Decimal('0.000145'),
            'comision_mensual': Decimal('14.00'),
            'tasa_cok': Decimal('0.115'),
            'tasa_ea_referencial': Decimal('0.078'),
        },
        {
            'nombre': 'Banco Azteca',
            'tasa_desgravamen': Decimal('0.000120'),
            'tasa_riesgo': Decimal('0.000170'),
            'comision_mensual': Decimal('18.00'),
            'tasa_cok': Decimal('0.13'),
            'tasa_ea_referencial': Decimal('0.090'),
        },
        {
            'nombre': 'Inbursa Bank Perú',
            'tasa_desgravamen': Decimal('0.000115'),
            'tasa_riesgo': Decimal('0.000165'),
            'comision_mensual': Decimal('16.50'),
            'tasa_cok': Decimal('0.125'),
            'tasa_ea_referencial': Decimal('0.0875'),
        },
    ]
    
    entidades_creadas = []
    for datos in entidades_data:
        entidad, created = EntidadFinanciera.objects.get_or_create(
            nombre=datos['nombre'],
            defaults={
                'tasa_desgravamen': datos['tasa_desgravamen'],
                'tasa_riesgo': datos['tasa_riesgo'],
                'comision_mensual': datos['comision_mensual'],
                'tasa_cok': datos['tasa_cok'],
                'tasa_ea_referencial': datos['tasa_ea_referencial'],
            }
        )
        status = "✓" if created else "  (ya existe)"
        print(f"  {status} {entidad.nombre}")
        entidades_creadas.append(entidad)
    
    return entidades_creadas


def crear_tasas_interes(entidades):
    """Las tasas se configuran en EntidadFinanciera, no en tabla separada"""
    print("\n📊 Tasas de interés configuradas en entidades")


def crear_bonos():
    """Crea bonos del buen pagador con los rangos correctos"""
    print("\n🎁 Creando bonos del buen pagador...")
    
    bonos_data = [
        {
            'valor_min': Decimal('68800'),
            'valor_max': Decimal('98100'),
            'monto': Decimal('27400'),
        },
        {
            'valor_min': Decimal('98101'),
            'valor_max': Decimal('146900'),
            'monto': Decimal('22800'),
        },
        {
            'valor_min': Decimal('146901'),
            'valor_max': Decimal('244600'),
            'monto': Decimal('20900'),
        },
        {
            'valor_min': Decimal('244601'),
            'valor_max': Decimal('362100'),
            'monto': Decimal('7800'),
        },
    ]
    
    contador = 0
    for datos in bonos_data:
        bono, created = BonoBuenPagador.objects.get_or_create(
            valor_vivienda_min=datos['valor_min'],
            valor_vivienda_max=datos['valor_max'],
            defaults={
                'monto_bono': datos['monto'],
                'moneda': 'PEN'
            }
        )
        
        if created:
            contador += 1
            print(f"  ✓ Bono S/ {datos['monto']} (S/ {datos['valor_min']:,} - S/ {datos['valor_max']:,})")
        else:
            print(f"  - Bono ya existe")
    
    print(f"  Total: {contador} bonos creados")


def crear_proyectos():
    """Crea proyectos inmobiliarios"""
    print("\n🏗️  Creando proyectos...")
    
    proyectos_data = [
        {
            'nombre_proyecto': 'Residencial Las Flores',
            'ubicacion': 'Lima, Surco',
            'descripcion': 'Proyecto residencial de lujo con 120 departamentos'
        },
        {
            'nombre_proyecto': 'Torres del Parque',
            'ubicacion': 'Lima, Miraflores',
            'descripcion': 'Edificios residenciales cerca del parque central'
        },
        {
            'nombre_proyecto': 'Condominio Playas',
            'ubicacion': 'Cuzco, Centro',
            'descripcion': 'Proyecto residencial con vista a la plaza de armas'
        },
        {
            'nombre_proyecto': 'Residencial Campestre',
            'ubicacion': 'Arequipa, Cerro Colorado',
            'descripcion': 'Proyecto con casas y departamentos en zona tranquila'
        }
    ]
    
    proyectos_creados = []
    for datos in proyectos_data:
        proyecto, created = Proyecto.objects.get_or_create(
            nombre_proyecto=datos['nombre_proyecto'],
            defaults={
                'ubicacion': datos['ubicacion'],
                'descripcion': datos['descripcion']
            }
        )
        
        if created:
            print(f"  ✓ Proyecto '{datos['nombre_proyecto']}' creado")
        else:
            print(f"  - Proyecto '{datos['nombre_proyecto']}' ya existe")
        
        proyectos_creados.append(proyecto)
    
    return proyectos_creados


def crear_inmuebles(proyectos):
    """Crea inmuebles (propiedades) dentro de proyectos"""
    print("\n🏠 Creando inmuebles...")
    
    inmuebles_data = [
        {'proyecto': 'Residencial Las Flores', 'codigo': 'A-1', 'precio': Decimal('350000.00'), 'area': Decimal('85.50'), 'piso': 1},
        {'proyecto': 'Residencial Las Flores', 'codigo': 'A-2', 'precio': Decimal('360000.00'), 'area': Decimal('90.75'), 'piso': 2},
        {'proyecto': 'Residencial Las Flores', 'codigo': 'B-1', 'precio': Decimal('380000.00'), 'area': Decimal('95.00'), 'piso': 3},
        {'proyecto': 'Residencial Las Flores', 'codigo': 'B-2', 'precio': Decimal('390000.00'), 'area': Decimal('100.25'), 'piso': 4},
        
        {'proyecto': 'Torres del Parque', 'codigo': 'C-101', 'precio': Decimal('450000.00'), 'area': Decimal('110.50'), 'piso': 10},
        {'proyecto': 'Torres del Parque', 'codigo': 'C-102', 'precio': Decimal('460000.00'), 'area': Decimal('115.75'), 'piso': 10},
        {'proyecto': 'Torres del Parque', 'codigo': 'D-201', 'precio': Decimal('480000.00'), 'area': Decimal('120.00'), 'piso': 20},
        
        {'proyecto': 'Condominio Playas', 'codigo': 'E-1', 'precio': Decimal('280000.00'), 'area': Decimal('75.00'), 'piso': 5},
        {'proyecto': 'Condominio Playas', 'codigo': 'E-2', 'precio': Decimal('285000.00'), 'area': Decimal('78.50'), 'piso': 5},
        
        {'proyecto': 'Residencial Campestre', 'codigo': 'F-1', 'precio': Decimal('320000.00'), 'area': Decimal('200.00'), 'piso': None},
        {'proyecto': 'Residencial Campestre', 'codigo': 'F-2', 'precio': Decimal('330000.00'), 'area': Decimal('210.50'), 'piso': None},
    ]
    
    contador = 0
    for datos in inmuebles_data:
        proyecto = Proyecto.objects.get(nombre_proyecto=datos['proyecto'])
        
        inmueble, created = Inmueble.objects.get_or_create(
            proyecto=proyecto,
            codigo=datos['codigo'],
            defaults={
                'precio_venta': datos['precio'],
                'area_m2': datos['area'],
                'piso': datos['piso'],
                'moneda': 'PEN',
                'estado': 'DISPONIBLE'
            }
        )
        
        if created:
            contador += 1
    
    print(f"  ✓ {contador} inmuebles creados")


def crear_clientes():
    """Crea clientes de prueba"""
    print("\n👨‍👩‍👧‍👦 Creando clientes...")
    
    clientes_data = [
        {
            'dni_ruc': '12345678',
            'nombres': 'Juan',
            'apellidos': 'Gonzales Martínez',
            'ingreso_mensual': Decimal('5500.00'),
            'email': 'juan.gonzales@email.com',
            'telefono': '987654321'
        },
        {
            'dni_ruc': '87654321',
            'nombres': 'María',
            'apellidos': 'López Rodríguez',
            'ingreso_mensual': Decimal('6000.00'),
            'email': 'maria.lopez@email.com',
            'telefono': '987654322'
        },
        {
            'dni_ruc': '11223344',
            'nombres': 'Carlos',
            'apellidos': 'Sánchez García',
            'ingreso_mensual': Decimal('7200.00'),
            'email': 'carlos.sanchez@email.com',
            'telefono': '987654323'
        },
        {
            'dni_ruc': '55667788',
            'nombres': 'Ana',
            'apellidos': 'Fernández Díaz',
            'ingreso_mensual': Decimal('5800.00'),
            'email': 'ana.fernandez@email.com',
            'telefono': '987654324'
        },
        {
            'dni_ruc': '99887766',
            'nombres': 'Pedro',
            'apellidos': 'Morales Quispe',
            'ingreso_mensual': Decimal('6500.00'),
            'email': 'pedro.morales@email.com',
            'telefono': '987654325'
        }
    ]
    
    contador = 0
    for datos in clientes_data:
        cliente, created = Cliente.objects.get_or_create(
            dni_ruc=datos['dni_ruc'],
            defaults={
                'nombres': datos['nombres'],
                'apellidos': datos['apellidos'],
                'ingreso_mensual': datos['ingreso_mensual'],
                'email': datos['email'],
                'telefono': datos['telefono']
            }
        )
        
        if created:
            contador += 1
            print(f"  ✓ Cliente '{datos['nombres']} {datos['apellidos']}' creado")
        else:
            print(f"  - Cliente con DNI {datos['dni_ruc']} ya existe")
    
    print(f"  Total: {contador} clientes creados")


def main():
    """Función principal para generar todos los datos"""
    print("=" * 60)
    print("GENERADOR DE DATOS INICIALES - Mi Vivienda")
    print("=" * 60)
    
    try:
        crear_grupos_y_permisos()
        grupos = Group.objects.filter(name__in=['ADMIN', 'VENDEDOR'])
        crear_usuarios(grupos)
        entidades = crear_entidades_financieras()
        crear_bonos()
        proyectos = crear_proyectos()
        crear_inmuebles(proyectos)
        crear_clientes()
        
        print("\n" + "=" * 60)
        print("✅ DATOS INICIALES GENERADOS EXITOSAMENTE")
        print("=" * 60)
        print("\n👤 Usuarios creados (para login):")
        print("  - admin@mivivienda.com / Admin123456 (Administrador)")
        print("  - juan.perez@mivivienda.com / Juan123456 (Vendedor)")
        print("  - maria.garcia@mivivienda.com / Maria123456 (Vendedor)")
        print("  - carlos.lopez@mivivienda.com / Carlos123456 (Vendedor)")
        print("\n✓ Datos creados:")
        print("  - 2 grupos (ADMIN, VENDEDOR)")
        print("  - 4 usuarios en auth_user")
        print("  - 6 entidades financieras")
        print("  - 4 bonos del buen pagador")
        print("  - 4 proyectos inmobiliarios")
        print("  - 11 inmuebles de ejemplo")
        print("  - 5 clientes de prueba")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error al generar datos: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
