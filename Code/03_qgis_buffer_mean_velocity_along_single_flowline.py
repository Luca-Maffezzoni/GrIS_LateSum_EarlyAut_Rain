from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterRasterLayer
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFileDestination
from qgis.core import QgsCoordinateReferenceSystem
import processing


class CalcolaMediaLungoFlowLine(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterRasterLayer('Velocityadta', 'Velocity data', defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('fowline', 'Fow line', types=[QgsProcessing.TypeVectorLine], defaultValue=None))
        self.addParameter(QgsProcessingParameterFileDestination('AverageVelocity', 'Average velocity', optional=True, fileFilter='HTML files (*.html)', createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(3, model_feedback)
        results = {}
        outputs = {}

        # Buffer
        alg_params = {
            'DISSOLVE': False,
            'DISTANCE': 500,
            'END_CAP_STYLE': 0,
            'INPUT': parameters['fowline'],
            'JOIN_STYLE': 0,
            'MITER_LIMIT': 2,
            'SEGMENTS': 5,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Buffer'] = processing.run('native:buffer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Clip data by buffer
        alg_params = {
            'ALPHA_BAND': False,
            'CROP_TO_CUTLINE': True,
            'DATA_TYPE': 0,
            'EXTRA': '',
            'INPUT': parameters['Velocityadta'],
            'KEEP_RESOLUTION': False,
            'MASK': outputs['Buffer']['OUTPUT'],
            'MULTITHREADING': False,
            'NODATA': None,
            'OPTIONS': '',
            'SET_RESOLUTION': False,
            'SOURCE_CRS': QgsCoordinateReferenceSystem('EPSG:3413'),
            'TARGET_CRS': QgsCoordinateReferenceSystem('EPSG:3413'),
            'X_RESOLUTION': None,
            'Y_RESOLUTION': None,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ClipDataByBuffer'] = processing.run('gdal:cliprasterbymasklayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Statistiche raster
        alg_params = {
            'BAND': 1,
            'INPUT': outputs['ClipDataByBuffer']['OUTPUT'],
            'OUTPUT_HTML_FILE': parameters['AverageVelocity']
        }
        outputs['StatisticheRaster'] = processing.run('qgis:rasterlayerstatistics', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['AverageVelocity'] = outputs['StatisticheRaster']['OUTPUT_HTML_FILE']
        return results

    def name(self):
        return 'Calcola media lungo flow line'

    def displayName(self):
        return 'Calcola media lungo flow line'

    def group(self):
        return 'Clip data by buffer'

    def groupId(self):
        return 'Clip data by buffer'

    def createInstance(self):
        return CalcolaMediaLungoFlowLine()
