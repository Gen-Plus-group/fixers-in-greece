#!/usr/bin/env python3
"""
Script to optimize all new pages with improved layout and comprehensive intro content
"""

import os
import re

def optimize_film_producer_page():
    """Optimize the Film Producer page"""
    file_path = 'hire-film-producer/index.html'
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the introduction section with expanded content
        old_intro = r'        <!-- Introduction Section -->\s*<section class="py-16">\s*<div class="container mx-auto px-4">\s*<div class="max-w-4xl mx-auto">\s*<div class="mb-12">\s*<h2 class="text-3xl font-bold text-vietnam-orange mb-6">Lead Your Production with Proven Expertise & Global Support</h2>\s*<p class="text-lg leading-relaxed mb-6">\s*We connect you with experienced Film Producers based in over 100 countries\. Our producers bring unmatched expertise, operational precision, and cultural fluency to ensure your production runs smoothly from concept to delivery\.\s*</p>\s*</div>'
        
        new_intro = '''        <!-- Introduction Section -->
        <section class="py-16">
            <div class="container mx-auto px-4">
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-bold text-vietnam-orange mb-6">
                        Lead Your Production with Proven Expertise & Global Support
                    </h2>
                    <p class="text-xl text-gray-300 max-w-4xl mx-auto mb-8">
                        We connect you with experienced Film Producers based in over 100 countries. Our producers bring unmatched expertise, operational precision, and cultural fluency to ensure your production runs smoothly from concept to delivery.
                    </p>
                </div>
                
                <div class="grid md:grid-cols-2 gap-12 mb-16">
                    <div>
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-4">Operational Excellence</h3>
                        <p class="text-gray-300 leading-relaxed mb-6">
                            Our producers are seasoned professionals who excel at managing complex productions from development through post-production. They bring deep expertise in budget management, scheduling, crew coordination, and risk mitigation, ensuring your project stays on track and within budget while maintaining the highest creative standards.
                        </p>
                        <p class="text-gray-300 leading-relaxed">
                            With experience across diverse production environments, our producers understand the unique challenges of different markets and can navigate local regulations, cultural considerations, and logistical requirements. They serve as your trusted partners, providing strategic guidance and hands-on management throughout the entire production lifecycle.
                        </p>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-4">Global Network & Local Expertise</h3>
                        <p class="text-gray-300 leading-relaxed mb-6">
                            Our global network of producers combines international experience with deep local knowledge, enabling seamless production execution anywhere in the world. They maintain established relationships with key vendors, facilities, and talent in their respective markets, providing you with immediate access to the best resources and most competitive rates.
                        </p>
                        <p class="text-gray-300 leading-relaxed">
                            Whether you're producing a multi-location commercial campaign, an international co-production, or a local documentary, our producers bring the right combination of global perspective and local insight. They understand both the creative and business aspects of production, ensuring your project achieves its artistic vision while meeting commercial objectives.
                        </p>
                    </div>
                </div>'''
        
        content = re.sub(old_intro, new_intro, content, flags=re.DOTALL)
        
        # Fix FAQ section layout
        old_faq = r'<div class="max-w-4xl mx-auto">\s*<h2 class="text-3xl font-bold text-vietnam-orange mb-8 text-center">Film Producer FAQs</h2>'
        new_faq = '''<div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-bold text-vietnam-orange mb-4">Film Producer FAQs</h2>
                    <p class="text-xl text-gray-300 max-w-3xl mx-auto">
                        Common questions about hiring film producers through our global network.
                    </p>
                </div>
                <div class="max-w-4xl mx-auto">
                    <h2 class="sr-only">Film Producer FAQs</h2>'''
        
        content = re.sub(old_faq, new_faq, content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} - Optimized successfully")
        return True
        
    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def optimize_line_producer_page():
    """Optimize the Line Producer page"""
    file_path = 'hire-line-producer/index.html'
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace max-w-4xl with full width layout
        content = re.sub(r'<div class="max-w-4xl mx-auto">', '<div class="container mx-auto px-4">', content)
        
        # Add comprehensive intro content after the hero section
        hero_end = r'(</section>\s*<!-- Introduction Section -->)'
        intro_content = '''</section>

        <!-- Introduction Section -->
        <section class="py-16">
            <div class="container mx-auto px-4">
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-bold text-vietnam-orange mb-6">
                        Professional Line Producer Services Worldwide
                    </h2>
                    <p class="text-xl text-gray-300 max-w-4xl mx-auto mb-8">
                        We connect you with top-tier Line Producers for feature films, commercials, TV series, and special projects. Our vetted professionals bring proven expertise in budget management, scheduling, and operational excellence to ensure your production runs smoothly from pre-production through wrap.
                    </p>
                </div>
                
                <div class="grid md:grid-cols-2 gap-12 mb-16">
                    <div>
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-4">Budget Discipline & Creative Integrity</h3>
                        <p class="text-gray-300 leading-relaxed mb-6">
                            Our Line Producers are masters of financial stewardship, ensuring every dollar is maximized for on-screen value while maintaining the creative vision. They bring sophisticated budget tracking systems, cost-control strategies, and vendor negotiation expertise that can save productions 15-25% without compromising quality.
                        </p>
                        <p class="text-gray-300 leading-relaxed">
                            With deep understanding of production workflows, they identify potential cost overruns before they occur and implement preventive measures. Their experience across different budget scales—from indie features to major studio productions—ensures they can adapt their approach to your specific financial parameters and creative requirements.
                        </p>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-4">Complex Schedule Management</h3>
                        <p class="text-gray-300 leading-relaxed mb-6">
                            Managing multi-location shoots, coordinating hundreds of crew members, and balancing talent availability requires exceptional organizational skills. Our Line Producers excel at creating detailed production schedules that account for weather contingencies, permit restrictions, equipment logistics, and creative needs while maintaining realistic timelines.
                        </p>
                        <p class="text-gray-300 leading-relaxed">
                            They use advanced scheduling software and proven methodologies to optimize shooting sequences, minimize company moves, and ensure efficient use of locations and resources. Their proactive approach to schedule management helps prevent delays and keeps productions on track even when unexpected challenges arise.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Introduction Section'''
        
        content = re.sub(hero_end, intro_content, content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} - Optimized successfully")
        return True
        
    except Exception as e:
        print(f"❌ {file_path} - Error: {e}")
        return False

def main():
    """Optimize all new pages"""
    print("🚀 Optimizing new pages with improved layout and comprehensive content...")
    
    success_count = 0
    total_count = 2
    
    if optimize_film_producer_page():
        success_count += 1
    
    if optimize_line_producer_page():
        success_count += 1
    
    print(f"\n📊 Optimization completed: {success_count}/{total_count} pages optimized")
    
    if success_count == total_count:
        print("🎉 All pages have been successfully optimized!")
    else:
        print(f"⚠️  {total_count - success_count} pages had issues and may need manual review")

if __name__ == "__main__":
    main()
