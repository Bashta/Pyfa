# shipBonusHeavyAssaultMissileAllDamageMC2
#
# Used by:
# Ship: Rapier
# Ship: Scythe Fleet Issue
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Cruiser").level
    for damageType in ("em", "explosive", "kinetic", "thermal"):
        fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                        "{0}Damage".format(damageType), ship.getModifiedItemAttr("shipBonusMC2") * level)
