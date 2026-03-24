import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('PRETORIA UBER ANALYSIS - \nMusa Mhlambi | Data Engineering Portfolio 2026', fontsize=16)
is_rush_hour = df['minute_per_km'] > 1.8 
#chart 1 distance vs price

axes[0,0].scatter(df['distance_km'], df['price'],           # X=distance, Y=price
           c=is_rush_hour,                           # Color by rush hour (True/False)
           cmap='RdYlGn',                            # Red-Yellow-Green color map
           alpha=0.6, s=30,                          # 60% transparent, small dots
           label='All Rides')                        # Legend label
axes[0,0].set_title('Distance vs Price\nRed = Rush Hour (1.4x Surge)', 
          fontsize=14, fontweight='bold')           # Main title
axes[0,0].set_xlabel('Distance (km)', fontsize=12)              # X axis label
axes[0,0].set_ylabel('Fare Amount (R)', fontsize=12)            # Y axis label
axes[0,0].grid(True, alpha=0.3)                             # Light grid
axes[0,0].axhline(y=20, color='black', linestyle='--',     # R20 minimum line
            alpha=0.7, label='R20 Minimum Price')

# CHART 2: Distance vs Duration ✅
axes[0,1].scatter(df['distance_km'], df['duration_min'], 
                 c=is_rush_hour, cmap='RdYlGn', alpha=0.6, s=30)
axes[0,1].set_title('Distance vs Duration\nRed = Slower Traffic', fontweight='bold')
axes[0,1].set_xlabel('Distance (km)')
axes[0,1].set_ylabel('Duration (min)')
axes[0,1].grid(True, alpha=0.3)

 # CHART 3: Price Distribution 
axes[1,0].hist([df[~is_rush_hour]['price'], df[is_rush_hour]['price']], 
               bins=30, alpha=0.7, label=['Normal', 'Rush Hour'], color=['green', 'red'])
axes[1,0].set_title('Price Distribution', fontweight='bold')
axes[1,0].set_xlabel('Price (R)')
axes[1,0].set_ylabel('Number of Rides')
axes[1,0].legend()

# CHART 4: Insights Table 
normal_avg = df[~is_rush_hour]['price'].mean()
rush_avg = df[is_rush_hour]['price'].mean()
premium_pct = ((rush_avg/normal_avg)-1)*100

table_data = [
    ['Metric', 'Normal', 'Rush Hour', 'Difference'],
    ['Avg Price', f'R{normal_avg:.0f}', f'R{rush_avg:.0f}', f'{premium_pct:.0f}% ↑'],
    ['Rides', len(df[~is_rush_hour]), len(df[is_rush_hour]), f'{is_rush_hour.mean()*100:.0f}%']
]
axes[1,1].axis('off')
table = axes[1,1].table(cellText=table_data[1:], colLabels=table_data[0],
                       cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(12)
axes[1,1].set_title('BUSINESS INSIGHTS', fontweight='bold', pad=20)

plt.tight_layout()
plt.show()