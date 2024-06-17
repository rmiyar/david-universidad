from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AsesorAcademico(models.Model):
    id_asesor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'asesor_academico'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bibliografia(models.Model):
    id_bibliografia = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    id_autor = models.ForeignKey('BibliografiaAutor', models.DO_NOTHING, db_column='id_autor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bibliografia'


class BibliografiaAutor(models.Model):
    id_autor = models.IntegerField(primary_key=True)
    autor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    anio_publicacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'bibliografia_autor'


class CalificacionMateria(models.Model):
    id_materia = models.IntegerField(primary_key=True)
    materia = models.CharField(max_length=50)
    nota_obtenida = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'calificacion_materia'


class Calificaciones(models.Model):
    id_calificacion = models.IntegerField(primary_key=True)
    fecha_evaluacion = models.CharField(max_length=50)
    id_materia = models.ForeignKey(CalificacionMateria, models.DO_NOTHING, db_column='id_materia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calificaciones'


class Certificado(models.Model):
    id_certificado = models.IntegerField(primary_key=True)
    nombre_estudiante = models.CharField(max_length=50)
    apellido_estudiante = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)
    id_programa = models.ForeignKey('CertificadoPrograma', models.DO_NOTHING, db_column='id_programa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificado'


class CertificadoPrograma(models.Model):
    id_programa = models.IntegerField(primary_key=True)
    programa_estudio = models.CharField(max_length=50)
    promedio_calificaciones = models.CharField(max_length=50)
    fecha_emision = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'certificado_programa'


class ClaseHora(models.Model):
    id_hora = models.IntegerField(primary_key=True)
    hora_inicio = models.CharField(max_length=50)
    hora_finalizacion = models.CharField(max_length=50)
    dia_semana = models.CharField(max_length=50)
    aula_virtual = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'clase_hora'


class Curso(models.Model):
    id_curso = models.IntegerField(primary_key=True)
    creditos = models.CharField(max_length=50)
    plazas_disponibles = models.CharField(max_length=50)
    nivel_academico = models.CharField(max_length=50)
    id_materia = models.ForeignKey('CursoMateria', models.DO_NOTHING, db_column='id_materia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'


class CursoMateria(models.Model):
    id_materia = models.IntegerField(primary_key=True)
    materia = models.CharField(max_length=50)
    codigo_curso = models.CharField(max_length=50)
    plan_estudio = models.CharField(max_length=50)
    requisitos_previos = models.CharField(max_length=50)
    instrumentos = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'curso_materia'


class CursoMateriaEstudiantes(models.Model):
    curso_materia = models.OneToOneField(CursoMateria, models.DO_NOTHING, primary_key=True)  # The composite primary key (curso_materia_id, user_id) found, that is not supported. The first column is selected.
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'curso_materia_estudiantes'
        unique_together = (('curso_materia', 'user_id'),)


class CursoProfesor(models.Model):
    id_materia = models.OneToOneField(CursoMateria, models.DO_NOTHING, db_column='id_materia', primary_key=True)  # The composite primary key (id_materia, id_profesor) found, that is not supported. The first column is selected.
    id_profesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profesor')

    class Meta:
        managed = False
        db_table = 'curso_profesor'
        unique_together = (('id_materia', 'id_profesor'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estudiante(models.Model):
    id_estudiante = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    cedula = models.CharField(unique=True, max_length=20)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    usuario = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True, db_column='usuario_id' )



    class Meta:
        managed = True
        db_table = 'estudiante'
        
    def clean(self):
        # Verificar si el usuario ya está asociado a otro estudiante o profesor
        if self.usuario:
            if Estudiante.objects.filter(usuario=self.usuario).exclude(pk=self.pk).exists():
                raise ValidationError("Este usuario ya está vinculado a un estudiante.")
            if Profesor.objects.filter(usuario=self.usuario).exists():
                raise ValidationError("Este usuario ya está vinculado a un profesor.")    
        


class EstudianteCarrera(models.Model):
    id_carrera = models.IntegerField(primary_key=True)
    programa_estudio = models.CharField(max_length=50)
    fecha_inicio = models.CharField(max_length=50)
    fecha_graduacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estudiante_carrera'


class EstudianteEstado(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado_financiero = models.CharField(max_length=50)
    historial_academico = models.CharField(max_length=50)
    estado_matricula = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estudiante_estado'


class EvaluacionCalificacion(models.Model):
    id_calificacion = models.IntegerField(primary_key=True)
    calificacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'evaluacion_calificacion'


class EvaluacionDocente(models.Model):
    id_evaluacion = models.IntegerField(primary_key=True)
    comentarios = models.CharField(max_length=50)
    fecha_evaluacion = models.CharField(max_length=50)
    id_calificacion = models.ForeignKey(EvaluacionCalificacion, models.DO_NOTHING, db_column='id_calificacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluacion_docente'


class Eventos(models.Model):
    id_evento = models.IntegerField(primary_key=True)
    evento = models.CharField(max_length=50)
    tipo_evento = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    hora = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    participante = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'eventos'


class EventosAcademicos(models.Model):
    id_eventos_academic = models.IntegerField(primary_key=True)
    temas_tratar = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    id_evento = models.ForeignKey(Eventos, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventos_academicos'


class HorarioClases(models.Model):
    id_horario = models.IntegerField(primary_key=True)
    curso = models.CharField(max_length=50)
    id_hora = models.ForeignKey(ClaseHora, models.DO_NOTHING, db_column='id_hora', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horario_clases'


class LaboratorioHorario(models.Model):
    id_horario = models.IntegerField(primary_key=True)
    dia_semana = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    profesor_responsable = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'laboratorio_horario'


class LaboratorioMateriales(models.Model):
    id_materiales = models.IntegerField(primary_key=True)
    asignacion_practica = models.CharField(max_length=50)
    recursos_disponibles = models.CharField(max_length=50)
    herramientas = models.CharField(max_length=50)
    software = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'laboratorio_materiales'


class LaboratorioVirtual(models.Model):
    id_laboratorio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'laboratorio_virtual'


class Pagos(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    estado_pago = models.CharField(max_length=50)
    referencia_pago = models.CharField(max_length=50)
    id_metodo_pago = models.ForeignKey('PagosMetodo', models.DO_NOTHING, db_column='id_metodo_pago', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagos'


class PagosMetodo(models.Model):
    id_metodo_pago = models.IntegerField(primary_key=True)
    tipo_pago = models.CharField(max_length=50)
    detalle_transaccion = models.CharField(max_length=50)
    monto = models.CharField(max_length=50)
    fecha_pago = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pagos_metodo'


class PlanDepartamento(models.Model):
    id_departamento = models.IntegerField(primary_key=True)
    departamento = models.CharField(max_length=50)
    curso_obligatorio = models.CharField(max_length=50)
    creditos_requeridos = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'plan_departamento'


class PlanEstudio(models.Model):
    id_plan_estudio = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    cursos_electivos = models.CharField(max_length=50)
    id_horario = models.ForeignKey(HorarioClases, models.DO_NOTHING, db_column='id_horario', blank=True, null=True)
    id_laboratorio = models.ForeignKey(LaboratorioVirtual, models.DO_NOTHING, db_column='id_laboratorio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan_estudio'


class Profesor(models.Model):
    id_profesor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    id_historial = models.ForeignKey('ProfesorHistorial', models.DO_NOTHING, db_column='id_historial', blank=True, null=True)
    id_materia = models.ForeignKey(CursoMateria, models.DO_NOTHING, db_column='id_materia', blank=True, null=True)
    usuario = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True,  db_column='usuario_id')

    class Meta:
        managed = False
        db_table = 'profesor'
        
    def clean(self):
        # Verificar si el usuario ya está asociado a otro profesor o estudiante
        if self.usuario:
            if Profesor.objects.filter(usuario=self.usuario).exclude(pk=self.pk).exists():
                raise ValidationError("Este usuario ya está vinculado a un profesor.")
            if Estudiante.objects.filter(usuario=self.usuario).exists():
                raise ValidationError("Este usuario ya está vinculado a un estudiante.")
        


class ProfesorHistorial(models.Model):
    id_historial = models.IntegerField(primary_key=True)
    especialidad = models.CharField(max_length=50)
    experiencia_laboral = models.CharField(max_length=50)
    historial_educativo = models.CharField(max_length=50)
    cursos_impartidos = models.CharField(max_length=50)
    cargo_trabajo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'profesor_historial'


class ProgramaCarrera(models.Model):
    id_carrera = models.IntegerField(primary_key=True)
    carrera = models.CharField(max_length=50)
    requisitos_graduacion = models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)
    requisitos_admision = models.CharField(max_length=50)
    nivel_academico = models.CharField(max_length=50)
    curso_obligatorio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'programa_carrera'


class ProgramaEstudio(models.Model):
    id_programa = models.IntegerField(primary_key=True)
    objetivos_programa = models.CharField(max_length=50)
    competencias_adquiridas = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    id_carrera = models.ForeignKey(ProgramaCarrera, models.DO_NOTHING, db_column='id_carrera', blank=True, null=True)
    id_tutoria = models.ForeignKey('ProgramaTutoria', models.DO_NOTHING, db_column='id_tutoria', blank=True, null=True)
    id_plan_estudio = models.ForeignKey(PlanEstudio, models.DO_NOTHING, db_column='id_plan_estudio', blank=True, null=True)
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    id_recurso = models.ForeignKey('RecursoAdicional', models.DO_NOTHING, db_column='id_recurso', blank=True, null=True)
    id_bibliografia = models.ForeignKey(Bibliografia, models.DO_NOTHING, db_column='id_bibliografia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programa_estudio'


class ProgramaTutoria(models.Model):
    id_tutoria = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    objetivos = models.CharField(max_length=50)
    id_programa = models.ForeignKey('TutoriaPrograma', models.DO_NOTHING, db_column='id_programa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programa_tutoria'


class RecursoAdicional(models.Model):
    id_recurso = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    enlace_descarga = models.CharField(max_length=50)
    id_material = models.ForeignKey('RecursoMaterial', models.DO_NOTHING, db_column='id_material', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recurso_adicional'


class RecursoMaterial(models.Model):
    id_material = models.IntegerField(primary_key=True)
    autor = models.CharField(max_length=50)
    tipo_material = models.CharField(max_length=50)
    licencias = models.CharField(max_length=50)
    anio_publicacion = models.CharField(max_length=50)
    tema_relacionado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'recurso_material'


class TutoriaPrograma(models.Model):
    id_programa = models.IntegerField(primary_key=True)
    area_enfoque = models.CharField(max_length=50)
    tutor = models.CharField(max_length=50)
    evaluacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tutoria_programa'


class EstudianteMateria(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso_materia = models.ForeignKey(CursoMateria, on_delete=models.CASCADE)

    class Meta:
        db_table = 'estudiante_materia'
        unique_together = ('estudiante', 'curso_materia')  # Esto asegura que la combinación de estudiante y materia sea única