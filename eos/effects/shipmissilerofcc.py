# shipMissileRofCC
#
# Used by:
# Ships named like: Caracal (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    groups = ("Missile Launcher Heavy", "Missile Launcher Rapid Light", "Missile Launcher Heavy Assault")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "speed", ship.getModifiedItemAttr("shipBonusCC") * level)
