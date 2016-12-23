from SpecImports import *
LobbyParent = 10014
BoilerParent = 10030
PipeLeftParent = 10023
PipeRightParent = 10032
OilParent = 10034
ControlParent = 10037
DuctParent = 10036
PaintMixerStorageParent = 10660
EastCatwalkParent = 10661
WestCatwalkParent = 10662
CenterSiloOutsideBattleCellParent = 10663
CenterSiloBattleCellParent = 10064
CenterSiloParent = 20095
SigRoomParent = 20058
WestSiloParent = 20094
WestSiloBattleCellParent = 10047
EastSiloParent = 20096
EastSiloBattleCellParent = 10068
LobbyCell = 0
BoilerCell = 1
PipeLeftCell = 2
PipeRightCell = 3
OilCell = 4
ControlCell = 5
DuctCell = 6
CenterSiloCell = 7
SigRoomCell = 8
WestSiloCell = 9
EastSiloCell = 10
CenterSiloOutsideCell = 11
PaintMixerStorageCell = 12
EastCatwalkCell = 13
WestCatwalkCell = 14
BattleCells = {LobbyCell: {'parentEntId': LobbyParent,
             'pos': Point3(0, 0, 0)},
 BoilerCell: {'parentEntId': BoilerParent,
              'pos': Point3(0, 0, 0)},
 OilCell: {'parentEntId': OilParent,
           'pos': Point3(0, 0, 0)},
 ControlCell: {'parentEntId': ControlParent,
               'pos': Point3(0, 0, 0)},
 CenterSiloCell: {'parentEntId': CenterSiloBattleCellParent,
                  'pos': Point3(0, 0, 0)},
 PipeLeftCell: {'parentEntId': PipeLeftParent,
                'pos': Point3(0, 0, 0)},
 PipeRightCell: {'parentEntId': PipeRightParent,
                 'pos': Point3(0, 0, 0)},
 DuctCell: {'parentEntId': DuctParent,
            'pos': Point3(0, 0, 0)},
 SigRoomCell: {'parentEntId': SigRoomParent,
               'pos': Point3(0, 0, 0)},
 WestSiloCell: {'parentEntId': WestSiloBattleCellParent,
                'pos': Point3(0, 0, 0)},
 EastSiloCell: {'parentEntId': EastSiloBattleCellParent,
                'pos': Point3(-20, -10, 0)},
 CenterSiloOutsideCell: {'parentEntId': CenterSiloOutsideBattleCellParent,
                'pos': Point3(0, 0, 0)},
 PaintMixerStorageCell: {'parentEntId': PaintMixerStorageParent,
                'pos': Point3(0, 0, 0)},
 EastCatwalkCell: {'parentEntId': EastCatwalkParent,
                'pos': Point3(0, 0, 0)},
 WestCatwalkCell: {'parentEntId': WestCatwalkParent,
                'pos': Point3(0, 0, 0)}}
CogData = [{'type': 'cc',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 10,
  'battleCell': LobbyCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tf',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 10,
  'battleCell': LobbyCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 10,
  'battleCell': LobbyCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 10,
  'battleCell': LobbyCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tf',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 10,
  'battleCell': BoilerCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20076,
  'skeleton': 0},
 {'type': 'm',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 10,
  'battleCell': BoilerCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20077,
  'skeleton': 0},
 {'type': 'tf',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 11,
  'battleCell': BoilerCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
  {'type': 'tf',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 10,
  'battleCell': BoilerCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20078,
  'skeleton': 0},
 {'type': 'm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 10,
  'battleCell': OilCell,
  'pos': Point3(-6, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 11,
  'battleCell': OilCell,
  'pos': Point3(-2, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'gh',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 11,
  'battleCell': OilCell,
  'pos': Point3(2, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
  {'type': 'gh',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 10,
  'battleCell': OilCell,
  'pos': Point3(6, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'gh',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 11,
  'battleCell': ControlCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20039,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 10,
  'battleCell': ControlCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20049,
  'skeleton': 1},
 {'type': 'tf',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 10,
  'battleCell': ControlCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20075,
  'skeleton': 1},
  {'type': 'tf',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 10,
  'battleCell': ControlCell,
  'pos': Point3(-10, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'm',
  'parentEntId': CenterSiloParent,
  'boss': 1,
  'level': 12,
  'battleCell': CenterSiloCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'mh',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 11,
  'battleCell': CenterSiloCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tf',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 11,
  'battleCell': CenterSiloCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 11,
  'battleCell': CenterSiloCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'mh',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 10,
  'battleCell': WestSiloCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20097,
  'skeleton': 0},
 {'type': 'tf',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 11,
  'battleCell': WestSiloCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20098,
  'skeleton': 0},
 {'type': 'm',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 11,
  'battleCell': WestSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20099,
  'skeleton': 0},
  {'type': 'mh',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 10,
  'battleCell': WestSiloCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'mh',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 11,
  'battleCell': EastSiloCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20100,
  'skeleton': 0},
 {'type': 'mh',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 11,
  'battleCell': EastSiloCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20101,
  'skeleton': 0},
 {'type': 'm',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 10,
  'battleCell': EastSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20102,
  'skeleton': 0},
   {'type': 'm',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 10,
  'battleCell': EastSiloCell,
  'pos': Point3(8, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 10,
  'battleCell': PipeLeftCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20109,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 10,
  'battleCell': PipeLeftCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20110,
  'skeleton': 1},
 {'type': 'gh',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 10,
  'battleCell': PipeLeftCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20111,
  'skeleton': 1},
   {'type': 'gh',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 10,
  'battleCell': PipeLeftCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 10,
  'battleCell': PipeRightCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20106,
  'skeleton': 1},
 {'type': 'gh',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 10,
  'battleCell': PipeRightCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20107,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 10,
  'battleCell': PipeRightCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20108,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 10,
  'battleCell': PipeRightCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'mh',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 11,
  'battleCell': DuctCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20038,
  'skeleton': 0},
 {'type': 'mh',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 10,
  'battleCell': DuctCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20067,
  'skeleton': 0},
 {'type': 'm',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 10,
  'battleCell': DuctCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20068,
  'skeleton': 0},
 {'type': 'tf',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 10,
  'battleCell': DuctCell,
  'pos': Point3(-8, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 11,
  'battleCell': SigRoomCell,
  'pos': Point3(5, -10.75, 0),
  'h': 90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'tf',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 11,
  'battleCell': SigRoomCell,
  'pos': Point3(5, -3.25, 0),
  'h': 90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 11,
  'battleCell': SigRoomCell,
  'pos': Point3(5, 3.25, 0),
  'h': 90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'gh',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 11,
  'battleCell': SigRoomCell,
  'pos': Point3(5, 10.75, 0),
  'h': 90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': CenterSiloOutsideBattleCellParent,
  'boss': 0,
  'level': 11,
  'battleCell': CenterSiloOutsideCell,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId':CenterSiloOutsideBattleCellParent,
  'boss': 0,
  'level': 11,
  'battleCell': CenterSiloOutsideCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'm',
  'parentEntId': CenterSiloOutsideBattleCellParent,
  'boss': 0,
  'level': 11,
  'battleCell': CenterSiloOutsideCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'm',
  'parentEntId': CenterSiloOutsideBattleCellParent,
  'boss': 0,
  'level': 11,
  'battleCell': CenterSiloOutsideCell,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': PaintMixerStorageParent,
  'boss': 0,
  'level': 11,
  'battleCell': PaintMixerStorageCell,
  'pos': Point3(-6, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': PaintMixerStorageParent,
  'boss': 0,
  'level': 10,
  'battleCell': PaintMixerStorageCell,
  'pos': Point3(-2, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': PaintMixerStorageParent,
  'boss': 0,
  'level': 11,
  'battleCell': PaintMixerStorageCell,
  'pos': Point3(2, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': PaintMixerStorageParent,
  'boss': 0,
  'level': 10,
  'battleCell': PaintMixerStorageCell,
  'pos': Point3(6, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': EastCatwalkParent,
  'boss': 0,
  'level': 11,
  'battleCell': EastCatwalkCell,
  'pos': Point3(-6, -5, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': EastCatwalkParent,
  'boss': 0,
  'level': 10,
  'battleCell': EastCatwalkCell,
  'pos': Point3(-2, -5, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': EastCatwalkParent,
  'boss': 0,
  'level': 11,
  'battleCell': EastCatwalkCell,
  'pos': Point3(2, -5, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': EastCatwalkParent,
  'boss': 0,
  'level': 10,
  'battleCell': EastCatwalkCell,
  'pos': Point3(6, -5, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': WestCatwalkParent,
  'boss': 0,
  'level': 11,
  'battleCell': WestCatwalkCell,
  'pos': Point3(-6, -5, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': WestCatwalkParent,
  'boss': 0,
  'level': 10,
  'battleCell': WestCatwalkCell,
  'pos': Point3(-2, -5, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': WestCatwalkParent,
  'boss': 0,
  'level': 11,
  'battleCell': WestCatwalkCell,
  'pos': Point3(2, -5, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': WestCatwalkParent,
  'boss': 0,
  'level': 10,
  'battleCell': WestCatwalkCell,
  'pos': Point3(6, -5, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
ReserveCogData = [{}]