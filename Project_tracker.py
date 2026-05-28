# -*- coding: utf-8 -*-
"""


@author: Rouzbeh
"""
from datetime import datetime

# Vi endrer listenavn til milestones for å reflektere tidsplanlegging
milestones = []

def add_milestone(name, category, planned_date_str, actual_date_str, status):
    # Vi bruker datetime.strptime for å gjøre tekststrenger om til ekte dato-objekter
    planned_date = datetime.strptime(planned_date_str, "%Y-%m-%d")
    actual_date = datetime.strptime(actual_date_str, "%Y-%m-%d")
    
    # Regner ut Schedule Variance (avvik i dager)
    # Positivt tall betyr forsinkelse, negativt/null betyr på eller før tidsplanen
    delay_days = (actual_date - planned_date).days
    
    milestone = {
        "name": name,
        "category": category.upper(),
        "planned": planned_date,
        "actual": actual_date,
        "delay_days": delay_days,
        "status": status
    }
    milestones.append(milestone)

def analyze_schedule_portfolio():
    if not milestones:
        print("\n[NOTICE] No milestones registered in the portfolio.")
        return

    # ---  ADVANCED DELAY & TREND ENGINE ---
    
    # 1. Grunnleggende portefølje-beregninger (Kun positive dager teller som akkumulert forsinkelse)
    total_delay_days = sum([m['delay_days'] for m in milestones if m['delay_days'] > 0])
    avg_delay_days = sum([m['delay_days'] for m in milestones]) / len(milestones)
    
    # 2. Isoler kritiske flaskehalser (Forsinkelser over 14 dager)
    critical_bottlenecks = [m for m in milestones if m['delay_days'] > 14]
    
    # 3. Dynamisk trendanalyse basert på prosjektfaser/kategorier
    phase_delays = {}
    phase_counts = {}
    
    for m in milestones:
        phase = m['category']
        phase_delays[phase] = phase_delays.get(phase, 0) + m['delay_days']
        phase_counts[phase] = phase_counts.get(phase, 0) + 1
        
    # Regner ut gjennomsnittlig forsinkelse per fase
    phase_trends = {phase: phase_delays[phase] / phase_counts[phase] for phase in phase_delays}

    # ========================================================
    # OUTPUT: EXECUTIVE SCHEDULE INTELLIGENCE DASHBOARD
    # ========================================================
    print("\n" + "=" * 60)
    print("             EXECUTIVE SCHEDULE ANALYTICS BRIEFING            ")
    print("=" * 60)
    print(f"TOTAL CUMULATIVE PORTFOLIO DELAY : {total_delay_days} Days")
    print(f"AVERAGE MILESTONE DELAY          : {avg_delay_days:.1f} Days")
    print("-" * 60)
    
    print("📈 DELAY TRENDS BY PROJECT PHASE:")
    for phase, avg_phase_delay in phase_trends.items():
        status_icon =  if avg_phase_delay > 10 else ( if avg_phase_delay > 0 else )
        print(f"  {status_icon} {phase:15} | Avg Delay: {avg_phase_delay:4.1f} Days")
        
    print("-" * 60)
    print("CRITICAL PATH BOTTLENECKS (> 14 DAYS SLIPPAGE):")
    if critical_bottlenecks:
        for i, m in enumerate(critical_bottlenecks, start=1):
            print(f"  {i}. [{m['category']}] {m['name']} — DELAYED BY {m['delay_days']} DAYS")
            print(f"     Planned Baseline: {m['planned'].strftime('%Y-%m-%d')} | Actual: {m['actual'].strftime('%Y-%m-%d')}")
    else:
        print("  Clean Slate: No critical bottlenecks identified.")
    print("=" * 60)


# --- SEED DATA (Eksempeldata basert på ekte datoer: ÅRR-MÅNED-DAG) ---
add_milestone("Detail Design Sign-off", "Planning", "2026-05-01", "2026-05-20", "Completed")  # 19 dager forsinket (Kritisk!)
add_milestone("Steel Procurement", "Procurement", "2026-05-10", "2026-05-12", "Completed")    # 2 dager forsinket
add_milestone("Foundation Pouring", "Construction", "2026-05-15", "2026-05-14", "Completed")  # -1 dag (Før tidsplan!)
add_milestone("BIM Model Freeze", "Planning", "2026-04-01", "2026-04-25", "Completed")        # 24 dager forsinket (Kritisk!)

# Kjør den oppgraderte analysen
analyze_schedule_portfolio()
